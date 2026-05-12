# keyboards/premium_menu.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_premium_plans_keyboard() -> InlineKeyboardMarkup:
    """
    Membuat keyboard pilihan paket premium (1 minggu / 1 bulan).
    """
    buttons = [
        [
            InlineKeyboardButton(text="1 Minggu - Rp 15rb", callback_data="prem_plan_1_minggu")
        ],
        [
            InlineKeyboardButton(text="1 Bulan - Rp 45rb", callback_data="prem_plan_1_bulan")
        ],
        [
            InlineKeyboardButton(text="🔙 Kembali Ke Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_payment_methods_keyboard(plan: str) -> InlineKeyboardMarkup:
    """
    Membuat inline keyboard pilihan payment: OVO, DANA, QRIS.
    """
    buttons = [
        [
            InlineKeyboardButton(text="OVO", callback_data=f"pyp_{plan}_ovo"),
            InlineKeyboardButton(text="DANA", callback_data=f"pyp_{plan}_dana")
        ],
        [
            InlineKeyboardButton(text="QRIS", callback_data=f"pyp_{plan}_qris")
        ],
        [
            InlineKeyboardButton(text="🔙 Pilih Paket Lain", callback_data="btn_premium"),
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_proof_verification_keyboard() -> InlineKeyboardMarkup:
    """
    Kembali atau Konfirmasi Bukti Pembayaran ke Admin Kerja Cepat.
    """
    buttons = [
        [
            InlineKeyboardButton(text="Kirim Bukti Pembayaran", url="https://t.me/admin_kerjacepat_ai")
        ],
        [
            InlineKeyboardButton(text="🔙 Pilih Paket Lain", callback_data="btn_premium"),
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
