# import sqlite untuk database analytics -> analytics.db
import sqlite3

# import format waktu
from datetime import datetime

# lokasi database analisis utama
DB_PATH= "data/analytics.db"

# function untuk analisis dari terminal
def init_db():
                # koneksi ke database
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()

                # tabel events
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS events
                            (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id TEXT,
                                feature TEXT,
                                timestamp TEXT
                                )
                       """)
                conn.commit()
                conn.close()
init_db()

# function untuk menyimpan aktifitas user 
def save_events(user_id, feature):
                # koneksi -> database
                conn = sqlite3.connect(DB_PATH)
                # pengambil data dari database
                cursor = conn.cursor()
                # simpan aktivitas user ke table events yang udh dibuat diatas
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(
                "INSERT INTO events (user_id, feature, timestamp) VALUES (?, ?, ?)",
                (user_id, feature, now)
                )
                # simpan perubahan save_event
                conn.commit()
                # tutup koneksi ke database biar ga idup trus
                conn.close()
                print(f"\n{'─'*50}")
                print(f"  📊 ANALYTICS EVENT TERCATAT")
                print(f"{'─'*50}")
                print(f"  👤 User    : {user_id}")
                print(f"  🔧 Feature : {feature}")
                print(f"  🕐 Waktu   : {now}")
                print(f"{'─'*50}\n")

# Function untuk menampilkan data dan aktivitas user ke terminal
def show_events():
                # Koneksi ke database
                conn = sqlite3.connect(DB_PATH)
                # cursor untuk membaca database
                cursor = conn.cursor()
                # Perintah : Ambil semua data dari tabel events *= shortcut
                cursor.execute("SELECT * FROM events ORDER BY id DESC LIMIT 20")
                # Ambil data dari database, fetchall=ambil semua
                events = cursor.fetchall()
                conn.close()

                if not events:
                                print("\n  📭 Belum ada data analytics.\n")
                                return

                # Header tabel
                print(f"\n{'═'*70}")
                print(f"  📊 ANALYTICS — 20 EVENT TERAKHIR")
                print(f"{'═'*70}")
                print(f"  {'ID':<5} {'USER ID':<15} {'FEATURE':<18} {'TIMESTAMP':<20}")
                print(f"  {'─'*5} {'─'*15} {'─'*18} {'─'*20}")

                # Isi tabel
                for row in events:
                                ev_id, user_id, feature, timestamp = row
                                print(f"  {ev_id:<5} {str(user_id):<15} {feature:<18} {timestamp:<20}")

                print(f"{'═'*70}")
                print(f"  Total: {len(events)} event(s)\n")

show_events()