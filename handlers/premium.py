# handlers/premium.py
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.premium_menu import (
    get_premium_plans_keyboard,
    get_payment_methods_keyboard,
    get_proof_verification_keyboard
)
from services.payment_service import generate_payment_instruction
from utils.cleanup import safe_delete_message
from services.service_analytics import save_events

router = Router()

@router.callback_query(F.data == "btn_premium")
async def process_premium_menu(callback: CallbackQuery):
    """
    Menampilkan menu benefit upgrade premium dan daftar paket.
    """
    premium_text = (
        f"✨ <b>TINGKATKAN PENGALAMAN ANDA</b>\n\n"
        f"<blockquote>\n"
        f"Nikmati kebebasan penuh dengan layanan Premium kami:\n"
        f"<b>Tanpa Batas Harian</b> — Produktivitas tanpa henti.\n"
        f"<b>Prioritas Utama</b> — Respon cepat dalam sekejap.\n"
        f"<b>Kualitas Maksimal</b> — Hasil terbaik untuk tulisan Anda.\n"
        f"<b>Akses Eksklusif</b> — Jadilah yang pertama mencoba fitur baru.\n\n"
        f"</blockquote>\n"
        f"<b>Pilih paket yang sesuai untuk Anda:</b>"
    )
    
    try:
        await callback.message.edit_text(
            text=premium_text,
            reply_markup=get_premium_plans_keyboard(),
            parse_mode="HTML"
        )
    except Exception:
        await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=premium_text,
            reply_markup=get_premium_plans_keyboard(),
            parse_mode="HTML"
        )
    await callback.answer()

@router.callback_query(F.data.startswith("prem_plan_"))
async def process_select_plan(callback: CallbackQuery):
    """
    Menangani pendaftaran paket premium dan berlanjut ke pemilihan metode pembayaran.
    """
    plan = callback.data.replace("prem_plan_", "") # '1_minggu' atau '1_bulan'
    
    plan_name = "Premium 1 Minggu (Rp 15.000)" if plan == "1_minggu" else "Premium 1 Bulan (Rp 45.000)"
    
    payment_choice_text = (
        f"📦 <b>Paket Terpilih:</b> {plan_name}\n\n"
        f"Silakan pilih metode pembayaran yang paling nyaman bagi Anda:"
    )
    
    await callback.message.edit_text(
        text=payment_choice_text,
        reply_markup=get_payment_methods_keyboard(plan),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data.startswith("pyp_"))
async def process_payment_instruction(callback: CallbackQuery):
    """
    Menampilkan QRIS atau nomor transfer merchant setelah memilih metode pembayaran.
    """
    # format callback: pyp_{plan}_{method}
    parts = callback.data.split("_")
    plan = f"{parts[1]}_{parts[2]}" # '1_minggu' atau '1_bulan'
    method = parts[3] # 'ovo', 'dana', 'qris'
    
    instruction_text, credential = generate_payment_instruction(plan, method)
    
    await callback.message.edit_text(
        text=instruction_text,
        reply_markup=get_proof_verification_keyboard(),
        parse_mode="HTML"
    )
    save_events(callback.from_user.id, "btn_premium")

    await callback.answer()
