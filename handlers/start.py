# handlers/start.py

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.main_menu import get_main_menu_keyboard
from utils.helpers import get_user_data
from utils.cleanup import safe_delete_message
from services.service_analytics import save_events

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Menangani perintah /start dari user. Menyambut user.
    """

    user_id = message.from_user.id
    user_name = message.from_user.first_name or "Pengguna"

    # Daftarkan data user jika baru pertama menggunakan bot
    user_data = get_user_data(user_id)

    welcome_text = (
        f"⚡ <b>Kerja Cepat with AI</b>\n\n"
        f"Bantu kerja lebih cepat, tanpa ribet.\n\n"
        f"<blockquote>\n"
        f"Nama: {user_name}\n"
        f"ID: {user_id}\n"
        f"Sisa Hari Ini: {user_data['remaining_credits']}\n"
        f"Status: {user_data['plan']}\n"
        f"</blockquote>\n"
        f"Mulai Produktivitas kamu yuk..\n"
    )

    # Hapus pesan perintah user agar chat selalu bersih
    await safe_delete_message(message.bot, message.chat.id, message.message_id)

    await message.answer(
        text=welcome_text,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "back_home")
async def process_back_home(callback: CallbackQuery):
    """
    Kembali ke menu utama dari callback.
    """
    user_id = callback.from_user.id
    user_name = callback.from_user.first_name or "Pengguna"
    user_data = get_user_data(user_id)
    welcome_text = (
        f"⚡ <b>Kerja Cepat with AI</b>\n"
        f"Bantu kerja lebih cepat, tanpa ribet.\n\n"
        f"<blockquote>\n"
        f"Sisa Hari Ini: {user_data['remaining_credits']}\n"
        f"Status: {user_data['plan']}\n"
        f"</blockquote>\n"
        f"Mulai kerja sekarang..\n"
    )

    try:
        await callback.message.edit_text(
            text=welcome_text,
            reply_markup=get_main_menu_keyboard(),
            parse_mode="HTML"
        )
    except Exception:
        # Jika gagal edit_text, hapus pesan lama lalu kirim pesan baru
        await safe_delete_message(
            callback.bot,
            callback.message.chat.id,
            callback.message.message_id
        )

        await callback.message.answer(
            text=welcome_text,
            reply_markup=get_main_menu_keyboard(),
            parse_mode="HTML"
        )

    save_events(callback.from_user.id, "back_home")

    await callback.answer()

