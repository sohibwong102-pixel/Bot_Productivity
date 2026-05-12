import os
from dotenv import load_dotenv

# Load file konfigurasi .env
load_dotenv()

# Token Bot Telegram & Gemini API Key
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

# Path penyimpan data user berupa JSON
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
USER_DATA_FILE = os.path.join(DATA_DIR, "user_data.json")

# Pastikan folder data selalu terbuat otomatis di awal
os.makedirs(DATA_DIR, exist_ok=True)
