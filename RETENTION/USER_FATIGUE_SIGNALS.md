# USER_FATIGUE_SIGNALS.md

## PURPOSE

Dokumen ini berfungsi untuk mengidentifikasi sinyal-sinyal kelelahan (_fatigue_) pengguna dalam menggunakan bot PRODUCTIVITY*AI. Tujuannya adalah untuk mendeteksi penurunan minat atau hambatan tersembunyi sebelum user memutuskan untuk berhenti menggunakan bot atau melakukan \_silent churn*.

Dokumen ini digunakan oleh:

- UX_RETENTION
- INTERACTION_DESIGNER
- MANAGER_ORCHESTRATOR

---

## CORE FATIGUE MINDSET

User tidak tiba-tiba berhenti. Mereka perlahan merasa "lelah" karena akumulasi gesekan kecil yang tidak terdeteksi.

- **Fatigue is Cumulative**: Satu klik tambahan mungkin tidak terasa berat, tapi 10 klik tambahan setiap hari akan membuat user mencari alternatif yang lebih simpel.
- **Mental Battery**: Setiap interaksi menghabiskan energi mental user. Bot yang baik adalah bot yang mengisi ulang "baterai" tersebut dengan memberikan hasil cepat.
- **Detection over Reaction**: Lebih baik mendeteksi perlambatan interaksi sekarang daripada mencoba memanggil kembali user yang sudah menghapus chat bot.

---

## COGNITIVE OVERLOAD SIGNALS

Tanda user mulai merasa kewalahan dengan informasi:

- **Analysis Paralysis**: User berhenti lama di menu yang memiliki > 5 tombol pilihan.
- **Scanning Failure**: User menanyakan hal yang sebenarnya sudah tertulis di pesan (menandakan teks terlalu panjang atau tidak _scannable_).
- **Frequent Backtracking**: User terus-menerus menekan tombol "Kembali" karena bingung dengan struktur menu.

---

## INTERACTION EXHAUSTION PATTERNS

Pola yang menunjukkan user mulai malas berinteraksi:

- **Abrupt Completion**: User berhenti tepat setelah mendapatkan hasil utama tanpa mengeksplorasi opsi tambahan (misal: tidak klik "Regenerasi" atau "Gaya Lain").
- **Shortening Sessions**: Durasi interaksi yang semakin pendek dari hari ke hari.
- **Declining Command Depth**: User hanya menggunakan fitur paling dasar dan mulai mengabaikan fitur-fitur _advanced_ yang ditawarkan.

---

## SILENT RETENTION DEATH INDICATORS

Sinyal bahaya yang sering tidak terlihat di log standar:

- **The "Seen" Ghosting**: User membuka pesan dari bot tapi tidak memberikan input atau klik tombol apa pun selama berjam-jam.
- **Broken Habit Loops**: User yang biasanya menggunakan bot di jam tertentu (misal: jam 9 pagi) tiba-tiba melewatkan jadwal tersebut tanpa pola pengganti.
- **Muted Notification**: User tetap terdaftar tetapi semakin jarang merespons atau membuka interaction dari bot.

---

## MOMENTUM BREAK PATTERNS

Hal-hal yang merusak alur produktivitas user:

- **The "Wait & Forget"**: Loading yang terlalu lama (> 5 detik) membuat user pindah ke aplikasi lain dan lupa kembali ke bot.
- **Interruptive Prompts**: Munculnya pop-up atau pesan promosi/feedback di tengah-tengah alur kerja utama.
- **Unnecessary Confirmations**: Menanyakan "Apakah Anda yakin?" untuk hal-hal sepele yang bisa di-_undo_.

---

## NAVIGATION FATIGUE

Kelelahan akibat struktur navigasi:

- **Deep Nesting**: User harus klik > 3 kali untuk mencapai fitur yang paling sering mereka gunakan.
- **Visual Clutter Fatigue**: Chat history yang terlalu penuh membuat user lelah melakukan scroll ke atas untuk mencari referensi sebelumnya.
- **Context Loss**: User lupa mereka sedang berada di menu mana karena judul pesan tidak jelas.

---

## CTA FATIGUE

Kelelahan terhadap tombol ajakan aksi:

- **Choice Overload**: Terlalu banyak tombol dengan bobot visual yang sama dalam satu pesan.
- **Ambiguous Labeling**: Tombol dengan teks yang tidak jelas (misal: "Proses" vs "Lanjut" vs "Oke").
- **Repetitive CTAs**: Menampilkan tombol yang sama terus-menerus bahkan ketika konteksnya sudah berubah.

---

## TYPING FATIGUE

Kelelahan karena terlalu banyak mengetik:

- **Repetitive Input**: Bot menanyakan hal yang sama berulang kali padahal bisa disimpan di memory.
- **Manual Command Entry**: Memaksa user mengetik `/perintah` alih-alih menggunakan _inline buttons_.
- **Lack of Quick Replies**: Tidak memberikan pilihan jawaban cepat (Quick Replies) untuk input yang umum.

---

## EMOTIONAL EXHAUSTION FACTORS

Faktor emosional yang membuat user menjauh:

- **The "Nagging" Assistant**: Bot terasa cerewet, terlalu banyak memberikan penjelasan yang tidak diminta.
- **Robotic Coldness**: Jawaban yang terlalu kaku dan tidak empatik saat user mengalami error.
- **Unrewarded Effort**: User sudah mengetik panjang tapi AI memberikan hasil yang tidak relevan atau generic.

---

## ANTI-PATTERNS

Hindari melakukan hal ini saat mendeteksi fatigue:

- **Doubling Down on Notifications**: Mengirim lebih banyak pesan pengingat saat user mulai jarang merespons.
- **Forced Feedback**: Meminta rating atau survey tepat saat user sedang terburu-buru menyelesaikan tugas.
- **Guilt Tripping**: Menggunakan bahasa yang membuat user merasa bersalah karena jarang berkunjung.

---

## RECOVERY PRINCIPLES

Cara mengembalikan momentum user yang mulai lelah:

- **The "Rest" Mode**: Berikan opsi untuk menyederhanakan menu jika bot mendeteksi user hanya menggunakan satu fitur spesifik.
- **Instant Reset**: Tombol "Ulangi dari Awal" yang mudah diakses untuk membersihkan semua kebingungan navigasi.
- **Value Injection**: Berikan hasil instan atau tips singkat yang benar-benar membantu tanpa meminta input tambahan.
- **Interface Thinning**: Secara dinamis menyembunyikan fitur yang jarang digunakan user untuk mengurangi _visual noise_.

---

## FINAL DOCTRINE

User yang lelah adalah user yang selangkah lagi akan pergi. Jangan tunggu mereka protes; perhatikan bagaimana mereka bergerak.

"Bot yang hebat bukan bot yang bisa melakukan segalanya, tapi bot yang tahu kapan harus diam dan kapan harus mempermudah jalan bagi user yang sedang lelah."
