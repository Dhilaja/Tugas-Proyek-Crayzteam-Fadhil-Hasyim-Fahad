data_siswa = {}
total_pemasukan = 0
total_pengeluaran = 0


def tambah_siswa(nama):
    if nama not in data_siswa:
        data_siswa[nama] = {
            "bayar": 0,
            "denda": 0
        }


def catat_pembayaran(nama, jumlah, denda):
    global total_pemasukan

    if nama in data_siswa:
        data_siswa[nama]["bayar"] += jumlah
        data_siswa[nama]["denda"] += denda
        total_pemasukan += jumlah


def tambah_pengeluaran(jumlah):
    global total_pengeluaran
    total_pengeluaran += jumlah


def siswa_belum_bayar():
    return [nama for nama, data in data_siswa.items() if data["bayar"] == 0]


def laporan_kas():
    return total_pemasukan, total_pengeluaran