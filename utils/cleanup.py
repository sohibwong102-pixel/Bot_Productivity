from aiogram import Bot
import logging

async def safe_delete_message(bot: Bot, chat_id: int, message_id: int):
    """
    Menghapus pesan secara aman agar bot tidak crash apabila pesan
    sudah dihapus manual atau sudah kedaluwarsa.
    Menerapkan Safe Cleanup Pattern.
    """
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        # Abaikan error jika pesan gagal dihapus, menjaga stabilitas chat
        logging.debug(f"Gagal menghapus pesan {message_id} di chat {chat_id}: {e}")
