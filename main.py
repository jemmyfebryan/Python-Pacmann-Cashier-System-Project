import numpy as np
import pandas as pd
from Transaksi import Transaction

trnsct_123 = Transaction()


def TambahBarang():
    lagi = "1"
    print("\nSilakan masukkan barang yang ingin dibeli:")
    while lagi == "1":
        nama = input("Masukkan nama item = ")
        jumlah = input("Masukkan jumlah item = ")
        harga = input("Masukkan harga item = ")
        try:
            hargatotal = float(jumlah) * float(harga)
        except:
            hargatotal = 0
        trnsct_123.add_item(nama, jumlah, harga, float(hargatotal))
        lagi = input("Apakah anda ingin menambah barang lagi? (1: Iya, 0: Tidak) : ")
        print("")


def UbahBarang():
    lagi = "1"
    while lagi == "1":
        print("\nApa yang ingin anda ubah?")
        print("1. Nama Item <update_item_name>")
        print("2. Jumlah Item <update_item_qty>")
        print("3. Harga Item <update_item_price>")
        masukkan = input("Masukkan input : ")
        if masukkan == "1":
            nama = input("Masukkan nama item yang ingin diubah = ")
            namabaru = input("Masukkan nama baru item yang diubah = ")
            trnsct_123.update_item_name(nama, namabaru)
        elif masukkan == "2":
            nama = input("Masukkan nama item yang ingin diubah = ")
            jumlahbaru = input("Masukkan jumlah baru item yang diubah = ")
            trnsct_123.update_item_qty(nama, jumlahbaru)
        elif masukkan == "3":
            nama = input("Masukkan nama item yang ingin diubah = ")
            hargabaru = input("Masukkan harga baru item yang diubah = ")
            trnsct_123.update_item_price(nama, hargabaru)
        lagi = input("Apakah anda ingin mengubah barang lagi? (1: Iya, 0: Tidak) : ")
        if lagi == "0":
            print("")


def HapusBarang():
    lagi = "1"
    while lagi == "1":
        nama = input("\nMasukkan nama item yang ingin dihapus = ")
        trnsct_123.delete_item(nama)
        lagi = input("Apakah anda ingin menghapus barang lagi? (1: Iya, 0: Tidak) : ")
        if lagi == "0":
            print("")


def CekValid():
    adasalah = 0
    for i in range(len(trnsct_123.table)):
        for j in range(len(trnsct_123.table[i])):
            if trnsct_123.table[i][j] == "":
                adasalah = 1
    if trnsct_123.table == [] or adasalah == 1:
        return 0
    else:
        return 1


def CekPembelian():
    print("")
    if trnsct_123.table != []:
        df = pd.DataFrame(trnsct_123.table, columns=trnsct_123.colnames)
        df.index += 1
        print(df)
        print("")
        adasalah = 0
        for i in range(len(trnsct_123.table)):
            for j in range(len(trnsct_123.table[i])):
                if trnsct_123.table[i][j] == "":
                    print(
                        "Item ke-"
                        + str(i + 1)
                        + " memiliki "
                        + trnsct_123.colnames[j]
                        + " yang kosong!"
                    )
                    adasalah = 1
        if adasalah == 1:
            print("")
    else:
        print("Pembelian anda masih kosong!")
        print("")


selesai = "0"
print("Selamat Datang di Kasir 123 Jemmy")
while selesai == "0":
    print("Ada yang bisa dibantu?")
    print("1. Tambah Barang Pembelian <add_item>")
    print("2. Ubah Barang Pembelian <update_item>")
    print("3. Hapus Barang Pembelian <delete_item>")
    print("4. Cek Pembalian <check_order>")
    print("5. Ulangi Pembelian <reset_transaction>")
    print("6. Selesai")
    print("0. Batal")
    masukkan = input("Masukkan input : ")
    if masukkan == "1":
        TambahBarang()
    elif masukkan == "2":
        UbahBarang()
    elif masukkan == "3":
        HapusBarang()
    elif masukkan == "4":
        CekPembelian()
    elif masukkan == "5":
        trnsct_123.reset_transaction()
    elif masukkan == "6":
        if CekValid() == 1:
            # menghitung grand total
            grandtotal = 0
            for i in range(len(trnsct_123.table)):
                grandtotal += float(trnsct_123.table[i][3])

            # menciptakan struk
            print("\nBerikut merupakan struk anda!")
            print("===Kasir 123 Jemmy===")
            print(pd.DataFrame(trnsct_123.table, columns=trnsct_123.colnames))
            if grandtotal > 500000:
                print("Total Harga = " + str(grandtotal))
                grandtotal = grandtotal * 0.9
                print("Diskon (10%) = " + str(grandtotal * 0.1))
            elif grandtotal > 300000:
                print("Total Harga = " + str(grandtotal))
                grandtotal = grandtotal * 0.92
                print("Diskon (8%) = " + str(grandtotal * 0.08))
            elif grandtotal > 200000:
                print("Total Harga = " + str(grandtotal))
                grandtotal = grandtotal * 0.95
                print("Diskon (5%) = " + str(grandtotal * 0.05))
            print("Grand Total = " + str(grandtotal))
            print("Terima kasih telah berlanja di toko kami!")
            selesai = 1
        else:
            print("")
            print("Mohon maaf daftar pembelian anda belum valid!")
            print("")
    else:
        selesai = 1
        print("\nTerima kasih, Silakan datang kembali!")
