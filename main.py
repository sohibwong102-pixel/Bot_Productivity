# main.py
import asyncio
import logging
import warnings
import os
import signal
import sys
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, tools, premium, history, status

# ─── Suppress warning deprecation dari google.generativeai ───
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ─── Konfigurasi logging agar rapi dan mudah dibaca ───
logging.basicConfig(
    level=logging.INFO,
    format="  %(asctime)s │ %(levelname)-7s │ %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Suppres log verbose dari aiogram & httpx agar terminal tidak banjir
logging.getLogger("aiogram.event").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

def kill_duplicate_bots():
    """
    Otomatis mematikan instance bot lain yang masih jalan (menghindari TelegramConflictError).
    """
    current_pid = os.getpid()
    killed = 0
    try:
        import subprocess
        result = subprocess.run(
            ["pgrep", "-f", "python.*main.py"],
            capture_output=True, text=True
        )
        for pid_str in result.stdout.strip().split("\n"):
            if pid_str and int(pid_str) != current_pid:
                os.kill(int(pid_str), signal.SIGTERM)
                killed += 1
        if killed:
            logging.info(f"🧹 {killed} instance bot duplikat dihentikan.")
            import time
            time.sleep(1)  # Tunggu sebentar agar Telegram melepas polling lama
    except Exception:
        pass

async def main():
    """
    Fungsi entry point bot. Menginisialisasi modul, mendaftarkan semua sub-router handler,
    dan menyalakan polling Telegram secara terus menerus.
    """
    if not BOT_TOKEN or BOT_TOKEN.startswith("YOUR_") or BOT_TOKEN == "":
        logging.error("❌ Token Bot Telegram belum di-set pada file .env!")
        logging.error("Silakan ganti nilai BOT_TOKEN dengan token asli dari t.me/BotFather terlebih dahulu!")
        return

    # Matikan instance duplikat sebelum mulai polling
    kill_duplicate_bots()

    # Inisialisasi Bot & Dispatcher FSM
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Daftarkan semua register router handler Kerja Cepat AI
    dp.include_router(start.router)
    dp.include_router(tools.router)
    dp.include_router(premium.router)
    dp.include_router(history.router)
    dp.include_router(status.router)

    print(f"\n{'═'*50}")
    print(f"  ⚡ KERJA CEPAT WITH AI — BOT AKTIF")
    print(f"{'═'*50}")
    print(f"  🤖 Bot      : @kerjacepatai_bot")
    print(f"  📡 Mode     : Polling")
    print(f"  💬 Perintah : /start")
    print(f"{'═'*50}\n")
    
    try:
        # Menghapus webhook lama jika ada dan memulai bot dengan modus polling aman
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"❌ Terjadi fatal error pada bot runtime: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print(f"\n{'─'*50}")
        print(f"  👋 Bot dimatikan secara manual.")
        print(f"{'─'*50}\n")
