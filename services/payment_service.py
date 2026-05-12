# services/payment_service.py

def generate_payment_instruction(plan: str, method: str) -> tuple[str, str]:
    """
    Menghasilkan detail tagihan dan instruksi pembayaran untuk peningkatan akun ke Premium.
    Mendukung OVO, DANA, dan QRIS secara instan.
    """
    harga = {
        "1_minggu": "Rp 15.000",
        "1_bulan": "Rp 45.000"
    }
    
    nama_paket = "Promo Akses Premium 1 Minggu (7 Hari)" if plan == "1_minggu" else "Promo Akses Premium 1 Bulan (30 Hari)"
    nominal = harga.get(plan, "Rp 15.000")

    instruction_text = (
        f"💳 *DETAIL INVOICE PEMBAYARAN PREMIUM*\n"
        f"────────────────────────────\n"
        f"📦 *Paket:* {nama_paket}\n"
        f"💰 *Total Tagihan:* {nominal}\n"
        f"📱 *Metode Transfer:* {method.upper()}\n"
        f"────────────────────────────\n"
        f"✍️ *Langkah-langkah Pembayaran:*\n\n"
    )

    if method == "qris":
        instruction_text += (
            "1. Scan kode QRIS kerja cepat berikut menggunakan aplikasi GoPay, OVO, ShopeePay, DANA, LinkAja atau m-Banking Anda.\n"
            "2. Masukkan nominal tagihan tepat sebesar yang tertera di atas.\n"
            "3. Lakukan konfirmasi pembayaran.\n\n"
            "🖼️ *KODE QRIS MERCHANT:* \n`[MOCK_QRIS_REGISTERED_MERCHANT_KEY]`"
        )
        mock_credential = "[MOCK_QRIS_PAYLOAD]"
    elif method == "ovo":
        instruction_text += (
            "1. Buka aplikasi OVO Anda.\n"
            "2. Transfer saldo Anda ke nomor OVO Merchant Kerja Cepat AI:\n"
            "   👉 *0812-3456-7890* (a.n. Kerja Cepat AI)\n"
            "3. Pastikan nominal transfer sesuai harga paket pilihan Anda.\n"
            "4. Simpan tangkapan layar bukti transfer."
        )
        mock_credential = "0812-3456-7890"
    elif method == "dana":
        instruction_text += (
            "1. Buka aplikasi DANA Anda.\n"
            "2. Pilih Kirim Saldo ke nomor DANA kami:\n"
            "   👉 *0812-3456-7890* (a.n. Kerja Cepat AI)\n"
            "3. Masukkan nominal pembayaran.\n"
            "4. Simpan tangkapan layar bukti transfer Anda jika sudah berhasil."
        )
        mock_credential = "0812-3456-7890"
    else:
        instruction_text += "Maaf, metode pembayaran yang Anda pilih tidak didukung."
        mock_credential = ""

    instruction_text += (
        "\n\n⚡ *PENTING:*\n"
        "Setelah transfer sukses, klik tombol *'💬 Kirim Bukti ke Admin'* di bawah untuk mengirimkan screenshot transaksi ke Customer Support kami.\n"
        "Status akun premium Anda akan diaktivasi dalam beberapa menit sesudah diverifikasi! 🚀"
    )

    return instruction_text, mock_credential
