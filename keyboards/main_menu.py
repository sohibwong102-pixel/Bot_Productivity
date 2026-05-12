# keyboards/main_menu.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Membuat inline keyboard utama untuk navigasi bot.
    Menghubungkan ke Tools, Riwayat, Status, dan Premium.
    """
    buttons = [
        [
            InlineKeyboardButton(text="Tools", callback_data="menu_tools"),
            InlineKeyboardButton(text="History", callback_data="btn_history")
        ],
        [
            InlineKeyboardButton(text="Status", callback_data="btn_status"),
            InlineKeyboardButton(text="Premium", callback_data="btn_premium")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
