# services/ai_service.py
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import google.generativeai as genai
import asyncio
from config import GEMINI_API_KEY

# Inisialisasi API Key. Model gemini-1.5-flash sangat cocok karena instan & cepat.
if GEMINI_API_KEY and not GEMINI_API_KEY.startswith("YOUR_"):
    genai.configure(api_key=GEMINI_API_KEY)

async def generate_productivity_result(tool: str, text: str, style: str) -> str:
    """
    Menghubungkan aplikasi ke API Gemini dengan request & prompt yang terstruktur rapi.
    Menerapkan 6 Fitur Utama dan 6 Gaya Tulisan Cepat.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY.startswith("YOUR_") or GEMINI_API_KEY == "":
        # Menyediakan fallback simulasi jika API key belum dikonfigurasi oleh user
        simulated_responses = {
            "rewrite": f"Berikut adalah versi tulisan baru Anda dengan gaya {style}:\n\n➡️ \"{text}\" dioptimalkan agar terdengar lebih {style} dan profesional untuk kebutuhan harian Anda.",
            "customer reply": f"Halo Kak! Terima kasih banyak sudah menghubungi kami. Menjawab pertanyaan Anda mengenai:\n\n\"{text}\"\n\nKami akan segera memproses detail ini secara {style} dan terbaik untuk kenyamanan Anda. Ada hal lain yang bisa kami bantu?",
            "caption generator": f"✨ [CAPTION INSTAN - GAYA {style.upper()}] ✨\n\n🎯 Mengulas ide mengenai: \"{text}\"\n\nYuk bagikan momen ini sekarang juga! Bagus banget buat bahan interaksi followers Anda. \n\n#KerjaCepat #Productivity #AIAsistan",
            "translate": f"Berikut hasil terjemahan instan gratis ke Gaya {style}:\n\n📝 \"{text}\" diterjemahkan secara natural dan nyaman dibaca.",
            "summarize": f"📌 *RINGKASAN UTAMA ({style.upper()})*\n\nDari teks yang Anda berikan:\n- Poin utama mengenai \"{text}\" berhasil disarikan secara padat dan ringkas sehingga menghemat waktu baca hingga 80%!",
            "email writer": f"Subject: Tindak Lanjut Mengenai {text[:30]}...\n\nDengan hormat,\n\nMelalui pesan email ini, kami ingin menyampaikan rangkuman perihal \"{text}\" dengan penyampaian secara {style}.\n\nDemikian pesan ini kami sampaikan. Terima kasih atas perhatian Anda.\n\nHormat kami,\nSobat Kerja AI"
        }
        return simulated_responses.get(tool.lower(), f"Berikut hasil simulasi pengolahan AI ({tool} - {style}):\n\n\"{text}\"\n\n(Catatan: Konfigurasikan file .env dengan GEMINI_API_KEY asli untuk hasil generasi dinamis)")

    # Menyiapkan system prompt berdasarkan Fitur yang dipilih
    system_prompts = {
        "rewrite": "Tugas Anda adalah menulis ulang teks berikut dengan versi kata yang baru, segar, dan lebih efektif.",
        "customer reply": "Tugas Anda adalah membalas chat / pesan keluhan atau pertanyaan customer ini secara ramah, solutif, empati, dan sigap.",
        "caption generator": "Tugas Anda adalah membuat caption media sosial yang memikat, interaktif, dan dilengkapi dengan hashtag relevan.",
        "translate": "Tugas Anda adalah menterjemahkan teks berikut dengan akurat ke bahasa Indonesia (jika teks asing) atau ke bahasa Inggris (jika teks aslinya Indonesia).",
        "summarize": "Tugas Anda adalah merangkum teks panjang / artikel berikut menjadi beberapa butir poin penting yang mudah dipahami.",
        "email writer": "Tugas Anda adalah menyusun draf email bisnis yang lengkap, terstruktur rapi dari opening hingga closing (termasuk baris Subject email)."
    }

    # Menyiapkan instruksi spesifik berdasarkan Gaya Tulisan yang dipilih
    style_instructions = {
        "formal": "Gunakan gaya bahasa formal, baku sesuai EYD, sopan, serius, dan menggunakan kosakata resmi.",
        "friendly": "Gunakan bahasa santai, hangat, bersahabat, penuh empati, akrab (seperti menggunakan sapaan Kak/Sobat), dan nyaman didengar.",
        "selling": "Gunakan teknik copywriting persuasif, menyoroti keunggulan, memicu rasa ingin tahu pembaca, dan akhiri dengan call-to-action (CTA).",
        "singkat": "Tuliskan hasil sepadat mungkin, hilangkan penjelasan bertele-tele, langsung menuju poin terpenting saja.",
        "profesional": "Gunakan pembawaan profesional, kompeten, objektif, meyakinkan, cocok untuk iklim dunia kerja dan bisnis modern.",
        "rapihin text": "Rapikan pengetikan teks, koreksi ejaan yang salah/typo, benahi susunan tulisan tanpa menambah info luar."
    }

    tool_key = tool.lower().strip()
    style_key = style.lower().strip()

    # Fallback key mapping if needed
    if "caption" in tool_key:
         tool_key = "caption generator"

    prompt_base = system_prompts.get(tool_key, "Tugas Anda adalah mendesain penulisan teks ini secara optimal.")
    style_guide = style_instructions.get(style_key, "Gunakan gaya penulisan standar yang rapi dan menarik.")

    full_prompt = f"""
{prompt_base}

Instruksi Tambahan Gaya Penulisan:
- {style_guide}
- WAJIB memberikan hasil akhir tulisan secara instan langsung pada poin jawaban utama, tanpa kalimat pembuka basa-basi dari asisten AI (seperti mengulangi 'Tentu, ini hasil tulisannya:').
- Buat agar tulisan tetap mengalir natural dan bernilai guna tinggi.

Teks Input dari Pengguna:
\"\"\"
{text}
\"\"\"

Hasil:
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Eksekusi generator sinkron di thread pool agar asinkron & non-blocking
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: model.generate_content(full_prompt)
        )
        return response.text.strip()
    except Exception as e:
        return f"❌ Terjadi kendala teknis saat menghubungkan ke AI: {str(e)}"
