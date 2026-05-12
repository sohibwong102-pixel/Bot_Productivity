# handlers/tools.py
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.tools_menu import get_tools_menu_keyboard
from keyboards.styles_menu import get_styles_keyboard, get_quick_action_keyboard
from states.tool_states import ToolStates
from services.ai_service import generate_productivity_result
from utils.helpers import get_user_data, add_user_history
from utils.cleanup import safe_delete_message
from services.service_analytics import save_events

router = Router()

# Menterjemahkan kode singgkat ke nama rapih yang ditampilkan
TOOL_MAP_CODE_TO_NAME = {
    "rw": "Rewrite",
    "cr": "Customer Reply",
    "cp": "Caption Generator",
    "tr": "Translate",
    "sm": "Summarize",
    "em": "Email Writer"
}

STYLE_MAP_CODE_TO_NAME = {
    "for": "Formal",
    "frd": "Friendly",
    "sel": "Selling Copy",
    "skt": "Singkat",
    "pro": "Profesional",
    "rap": "Rapihin Text"
}

@router.callback_query(F.data == "menu_tools")
async def show_tools_menu(callback: CallbackQuery, state: FSMContext):
    """
    Menampilkan daftar 6 Core Tools AI yang tersedia.
    """
    await state.clear() # bersihkan state lama agar aman
    
    text_menu = (
        "<b>PRODUCTIVITY TOOLS</b>\n\n"
        "Pilih tools yang kamu butuhkan untuk menyempurnakan pekerjaan hari ini:"
    )
    
    try:
        await callback.message.edit_text(
            text=text_menu,
            reply_markup=get_tools_menu_keyboard(),
            parse_mode="HTML"
        )
    except Exception:
        await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=text_menu,
            reply_markup=get_tools_menu_keyboard(),
            parse_mode="HTML"
        )
    await callback.answer()

@router.callback_query(F.data.startswith("tool_"))
async def process_tool_selection(callback: CallbackQuery, state: FSMContext):
    """
    Tahap 1: User memilih tool, instruksikan user mengirimkan teks input.
    """
    tool_code = callback.data.replace("tool_", "") # 'rewrite', 'customer_reply', 'caption', 'translate', 'summarize', 'email_writer'
    
    # Konversi kode aseli ke singkatan agar callback aman dari batasan size payload telegram
    short_codes = {
        "rewrite": "rw",
        "customer_reply": "cr",
        "caption": "cp",
        "translate": "tr",
        "summarize": "sm",
        "email_writer": "em"
    }
    short_code = short_codes.get(tool_code, tool_code)
    tool_name = TOOL_MAP_CODE_TO_NAME.get(short_code, "AI Tool")

    # Masuk ke FSM state
    await state.set_state(ToolStates.waiting_for_input)
    await state.update_data(tool=short_code)

    prompt_text = (
        f"📝 <b>Tool Terpilih:</b> {tool_name}\n\n"
        f"Silakan kirimkan teks atau poin-poin yang ingin kamu olah. "
        f"kami siap membantu menyempurnakannya. 👇"
    )

    await callback.message.edit_text(
        text=prompt_text,
        parse_mode="HTML"
    )
    await callback.answer()

@router.message(ToolStates.waiting_for_input)
async def process_text_input(message: Message, state: FSMContext):
    """
    Tahap 2: User mengirim teks, periksa limit lalu minta user memilih gaya tulisan.
    """
    user_id = message.from_user.id
    user_text = message.text
    
    if not user_text:
        await message.answer("⚠️ Format salah, silakan kirimkan teks tertulis biasa saja.")
        return

    # Validasi limit harian
    user_data = get_user_data(user_id)
    usage = user_data.get("usage_today", 0)
    limit = user_data.get("daily_limit", 10)
    plan = user_data.get("plan", "Free")

    if plan == "Free" and usage >= limit:
        out_of_limit_text = (
            "⚠️ <b>Batas Harian Tercapai</b>\n\n"
            "Batas penggunaan harian untuk akun dasar telah terpenuhi.\n\n"
            "kembali besok, atau beralih ke <b>Premium</b> "
            "untuk kebebasan akses tanpa batas. 🚀"
        )
        from keyboards.premium_menu import get_premium_plans_keyboard
        await message.answer(
            text=out_of_limit_text,
            reply_markup=get_premium_plans_keyboard(),
            parse_mode="HTML"
        )
        await state.clear()
        return

    # Catat teks input ke context FSM
    await state.update_data(text=user_text)
    data = await state.get_data()
    tool_code = data.get("tool", "rw")
    tool_name = TOOL_MAP_CODE_TO_NAME.get(tool_code, "AI Tool")

    style_prompt = (
        f"🎨 <b>Pilih Gaya Tulisan</b>\n\n"
        f"Bagaimana kamu ingin {tool_name} ini disampaikan? Pilih salah satu opsi di bawah:"
    )

    # Bersihkan chat dengan menghapus input text mentah user agar rapi
    await safe_delete_message(message.bot, message.chat.id, message.message_id)

    # Kirim keyboard pilihan gaya bahasa
    await message.answer(
        text=style_prompt,
        reply_markup=get_styles_keyboard(tool_code),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("st_"))
async def process_style_generation(callback: CallbackQuery, state: FSMContext):
    """
    Tahap 3: Memicu AI untuk melakukan penulisan. Memberikan pesan loading yang nantinya di-delete otomatis.
    """
    parts = callback.data.split("_")
    tool_code = parts[1]
    style_code = parts[2]

    # Baca parameter dari state
    state_data = await state.get_data()
    text_input = state_data.get("text")

    if not text_input:
        await callback.message.edit_text(
            text="⚠️ <b>Sesi Berakhir</b>\n\nMaaf, sesi telah berakhir. Silakan pilih kembali tool yang ingin digunakan.",
            reply_markup=get_tools_menu_keyboard(),
            parse_mode="HTML"
        )
        await state.clear()
        await callback.answer()
        return

    # 1. Kirim pesan tunggu (Loading message - ditandai untuk dihapus nanti)
    loading_msg = await callback.message.answer(
        text="⏳ <b>Sedang diproses...</b>",
        parse_mode="HTML"
    )

    # 2. Hapus menu gaya agar layar tetap ringkas
    await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    # 3. Jalankan pengolahan dengan Gemini AI
    tool_name = TOOL_MAP_CODE_TO_NAME.get(tool_code, "General Task")
    style_name = STYLE_MAP_CODE_TO_NAME.get(style_code, "Standard")
    
    ai_result = await generate_productivity_result(tool_name, text_input, style_name)

    # 4. Rekam Riwayat Kerja di file JSON local
    user_id = callback.from_user.id
    add_user_history(user_id, tool_name, text_input, ai_result, style_name)

    # Menyusun layout akhir output premium
    final_output = (
        f"✅ <b>HASIL KARYA AI</b>\n"
        f"<blockquote>\n"
        f"🛠️ <b>Tool:</b> {tool_name}\n"
        f"🎨 <b>Style:</b> {style_name}\n"
        f"</blockquote>\n\n"
        f"{ai_result}\n\n"
        f"────────────────────────────\n"
        f"✨ <i>Butuh penyesuaian? Gunakan fitur regenerasi atau pilih style lain di bawah ini.</i>"
    )

    # 5. Kirimkan hasil tulisan & tawarkan Quick Action
    await callback.message.answer(
        text=final_output,
        reply_markup=get_quick_action_keyboard(tool_code, style_code),
        parse_mode="HTML"
    )

    # 6. Hapus pesan tunggu/loading secara aman (Cleanup System)
    await safe_delete_message(callback.bot, loading_msg.chat.id, loading_msg.message_id)
    await callback.answer(text="Hasil tulisan berhasil diramu!")

@router.callback_query(F.data.startswith("act_regen_"))
async def process_regenerate(callback: CallbackQuery, state: FSMContext):
    """
    Quick Action: Memicu generasi ulang untuk input teks yang sama.
    """
    parts = callback.data.split("_")
    tool_code = parts[2]
    style_code = parts[3]

    state_data = await state.get_data()
    text_input = state_data.get("text")

    if not text_input:
        await callback.answer("⚠️ Sesi telah berakhir. Silakan masukkan kembali teks yang ingin Anda olah.", show_alert=True)
        return

    # Kirim loading sementara
    loading_msg = await callback.message.answer(
        text="🔄 <b>Menyempurnakan kembali tulisan Anda...</b> ⏳",
        parse_mode="HTML"
    )

    # Hapus layout hasil lama agar chat tidak bertumpuk berat
    await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    tool_name = TOOL_MAP_CODE_TO_NAME.get(tool_code, "AI Tool")
    style_name = STYLE_MAP_CODE_TO_NAME.get(style_code, "Standard")

    # Regenerate dengan Gemini AI
    ai_result = await generate_productivity_result(tool_name, text_input, style_name)

    # Rekam riwayat terbaru
    add_user_history(callback.from_user.id, tool_name, text_input, ai_result, style_name)

    regenerated_output = (
        f"✅ <b>HASIL GENERATE ULANG</b>\n"
        f"<blockquote>\n\n"
        f"🛠️ <b>Tool:</b> {tool_name}\n"
        f"🎨 <b>Style:</b> {style_name}\n\n"
        f"</blockquote>\n\n"
        f"{ai_result}\n\n"
        f"────────────────────────────\n"
        f"✨ <i>Variasi baru telah berhasil dibuat.</i>"
    )

    await callback.message.answer(
        text=regenerated_output,
        reply_markup=get_quick_action_keyboard(tool_code, style_code),
        parse_mode="HTML"
    )

    # Bersihkan loading message
    await safe_delete_message(callback.bot, loading_msg.chat.id, loading_msg.message_id)
    await callback.answer(text="Regenerasi sukses!")

@router.callback_query(F.data.startswith("act_otherstyle_"))
async def process_other_style_choice(callback: CallbackQuery, state: FSMContext):
    """
    Quick Action: Memilih gaya lain untuk tulisan yang sama tanpa ketik ulang.
    """
    tool_code = callback.data.split("_")[2]
    tool_name = TOOL_MAP_CODE_TO_NAME.get(tool_code, "AI Tool")

    style_prompt = (
        f"🎨 <b>Pilih Gaya Penulisan Alternatif</b>\n\n"
        f"Berikut adalah beberapa pilihan gaya penulisan lain untuk Anda. Silahkan pilih:"
    )

    # Hapus pesan hasil lama
    await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)

    await callback.message.answer(
        text=style_prompt,
        reply_markup=get_styles_keyboard(tool_code),
        parse_mode="HTML"
    )

    save_events(callback.from_user.id, "menu_tools")

    await callback.answer()
