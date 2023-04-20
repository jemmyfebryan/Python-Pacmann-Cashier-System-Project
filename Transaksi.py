import numpy as np


class Transaction:
    def __init__(self):
        self.table = []
        self.colnames = np.array(
            ["Nama Item", "Jumlah Item", "Harga/item", "Harga Total"]
        )

    def add_item(self, nama_item, jumlah_item, harga_item, harga_total):
        # Cek apakah nama item dengan harganya ada yang sama
        kembar = 0
        for i in range(len(self.table)):
            if self.table[i][0] == nama_item and self.table[i][2] == harga_item:
                self.table[i][1] = int(self.table[i][1]) + int(jumlah_item)
                kembar = 1

        # tambahkan biasa
        if kembar == 0:
            self.table.append([nama_item, jumlah_item, harga_item, harga_total])

    def update_item_name(self, nama_item_lama, nama_item_baru):
        ganti = 0
        for i in range(len(self.table)):
            if self.table[i][0] == nama_item_lama:
                self.table[i][0] = nama_item_baru  # Ubah nama item ke yang baru
                ganti = 1
        if ganti == 0:
            print("Tidak ada nama item yang diubah")

    def update_item_qty(self, nama_item, jumlah_item_baru):
        ganti = 0
        for i in range(len(self.table)):
            if self.table[i][0] == nama_item:
                self.table[i][1] = jumlah_item_baru  # Ubah jumlah item ke yang baru
                try:
                    self.table[i][3] = float(self.table[i][1]) * float(
                        self.table[i][2]
                    )  # Ubah harga total item ke yang baru
                except:
                    self.table[i][3] = 0
                ganti = 1
        if ganti == 0:
            print("Tidak ada jumlah item yang diubah")

    def update_item_price(self, nama_item, harga_item_baru):
        ganti = 0
        for i in range(len(self.table)):
            if self.table[i][0] == nama_item:
                self.table[i][2] = harga_item_baru  # Ubah harga item ke yang baru
                try:
                    self.table[i][3] = float(self.table[i][1]) * float(
                        self.table[i][2]
                    )  # Ubah harga total item ke yang baru
                except:
                    self.table[i][3] = 0
                ganti = 1
        if ganti == 0:
            print("Tidak ada harga item yang diubah")

    def delete_item(self, nama_item):
        ganti = 0
        try:
            n = 0
            for i in range(len(self.table)):
                if self.table[i - n][0] == nama_item:
                    self.table = list(np.delete(self.table, i - n, 0))
                    n += 1
                    ganti = 1
        except:
            pass
        if ganti == 0:
            print("Nama item yang ingin dihapus tidak ditemukan!")

    def reset_transaction(self):
        self.table = []
        print("")
        print("Daftar pembelian telah dibersihkan!")
        print("")
