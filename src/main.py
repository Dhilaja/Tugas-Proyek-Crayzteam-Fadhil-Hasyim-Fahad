from kas_logic import hitung_denda, hitung_saldo
from data_manager import *

def menu():
    while True:
        print("\n=== SISTEM KAS KELAS ===")
        print("1. Tambah Siswa")
        print("2. Catat Pembayaran")
        print("3. Tambah Pengeluaran")
        print("4. Lihat Siswa Belum Bayar")
        print("5. Lihat Laporan Kas")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama siswa: ")
            tambah_siswa(nama)
            print("Siswa berhasil ditambahkan!")

        elif pilihan == "2":
            nama = input("Nama siswa: ")
            jumlah = int(input("Jumlah bayar: "))
            hari_telat = int(input("Hari telat: "))
            denda = hitung_denda(hari_telat)
            catat_pembayaran(nama, jumlah, denda)
            print("Pembayaran dicatat. Denda:", denda)

        elif pilihan == "3":
            jumlah = int(input("Jumlah pengeluaran: "))
            tambah_pengeluaran(jumlah)
            print("Pengeluaran dicatat!")

        elif pilihan == "4":
            belum = siswa_belum_bayar()
            print("Siswa belum bayar:", belum)

        elif pilihan == "5":
            masuk, keluar = laporan_kas()
            saldo = hitung_saldo(masuk, keluar)
            print("Total Masuk:", masuk)
            print("Total Keluar:", keluar)
            print("Saldo Akhir:", saldo)

        elif pilihan == "6":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()