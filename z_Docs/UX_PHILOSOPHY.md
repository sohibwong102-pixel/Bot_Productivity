# UX_PHILOSOPHY.md - Filosofi Pengalaman Pengguna

Dokumen ini mendefinisikan identitas visual dan gaya komunikasi **Kerja Cepat AI**. Tujuannya adalah menciptakan bot yang terasa premium, efisien, dan bersahabat.

## 🎯 Target Feeling
Bot ini harus terasa:
- **Warm**: Hangat dan membantu, bukan robot kaku.
- **Premium**: Desain rapi dengan penggunaan tipografi (bold/italic/blockquote) yang cerdas.
- **Fast & Efficient**: Langsung ke inti jawaban tanpa basa-basi.
- **Modern & Non-Corporate**: Bahasa yang santai tapi profesional, menghindari istilah "korporat" yang membosankan.

## 🧠 Prinsip Utama

### 1. Chat Cleanliness (Kebersihan Chat)
- **Zero Spam**: Jangan biarkan chat history bertumpuk dengan menu lama.
- **Auto-Cleanup**: Gunakan `safe_delete_message` untuk menghapus pesan perintah user atau pesan loading segera setelah hasil diberikan.
- **Edit vs New**: Utamakan mengedit pesan yang sudah ada (`edit_text`) daripada mengirim pesan baru jika hanya berpindah menu.

### 2. Gaya Komunikasi
- **Anti-Basa-Basi**: AI harus langsung memberikan hasil tulisan. Hindari: "Tentu, ini adalah hasil tulisan ulang Anda:".
- **Sapaan**: Gunakan "Kak" atau "Sobat" untuk kesan akrab (Friendly style), namun tetap gunakan bahasa formal yang rapi untuk gaya Formal/Profesional.
- **Emoji Usage**: Gunakan emoji secara minimalis (1-2 per pesan). Gunakan emoji hanya untuk penanda visual (misal: 📝, ✅, ⚠️), bukan hiasan berlebihan.

### 3. Kecepatan & Retensi
- **Loading Message**: Selalu berikan indikator "Sedang diproses..." agar user tahu bot tidak sedang hang. Hapus segera setelah selesai.
- **CTA (Call to Action)**: Berikan tombol langkah selanjutnya yang relevan (misal: "Regenerasi" atau "Gaya Lain") agar user terus berinteraksi tanpa bingung.

## ❌ Hal yang Harus Dihindari
- **Robotic Responses**: Jawaban yang terasa dihasilkan oleh template kaku.
- **Excessive Introduction**: Penjelasan panjang lebar tentang cara kerja bot di setiap menu.
- **Spammy CTA**: Terlalu sering memaksa user untuk upgrade ke Premium di setiap kesempatan.
- **Long Blocks of Text**: Gunakan `<blockquote>` atau bullet points untuk memecah teks panjang agar mudah dipindai (scannable).
