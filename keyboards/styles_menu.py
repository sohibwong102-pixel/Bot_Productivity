# keyboards/styles_menu.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_styles_keyboard(tool_code: str) -> InlineKeyboardMarkup:
    """
    Membuat inline keyboard untuk memilih 1 dari 6 Gaya Tulisan Cepat.
    tool_code: 'rw', 'cr', 'cp', 'tr', 'sm', 'em'
    """
    buttons = [
        [
            InlineKeyboardButton(text="Formal", callback_data=f"st_{tool_code}_for"),
            InlineKeyboardButton(text="Friendly", callback_data=f"st_{tool_code}_frd")
        ],
        [
            InlineKeyboardButton(text="Selling", callback_data=f"st_{tool_code}_sel"),
            InlineKeyboardButton(text="Singkat", callback_data=f"st_{tool_code}_skt")
        ],
        [
            InlineKeyboardButton(text="Profesional", callback_data=f"st_{tool_code}_pro"),
            InlineKeyboardButton(text="Rapihin", callback_data=f"st_{tool_code}_rap")
        ],
        [
            InlineKeyboardButton(text="🔙 Tools", callback_data="menu_tools"),
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_quick_action_keyboard(tool_code: str, style_code: str) -> InlineKeyboardMarkup:
    """
    Membuat inline keyboard Quick Action setelah hasil AI berhasil dibuat.
    """
    buttons = [
        [
            InlineKeyboardButton(text="🔄 Regenerate", callback_data=f"act_regen_{tool_code}_{style_code}"),
            InlineKeyboardButton(text="Style Lain", callback_data=f"act_otherstyle_{tool_code}")
        ],
        [
            InlineKeyboardButton(text="🔙 Tools", callback_data="menu_tools"),
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
