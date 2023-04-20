# Python-Pacmann-Cashier-System-Project

## Latar Belakang
Andi memiliki kebutuhan untuk meningkatkan proses bisnis di supermarket miliknya. Salah satu solusinya adalah dengan membuat sistem kasir self-service yang memungkinkan pelanggan untuk memasukkan sendiri informasi tentang barang yang dibeli seperti jumlah dan harga, bahkan jika pelanggan berasal dari kota lain. Sebagai programmer, tugas saya adalah untuk membuat program "Super Cashier" yang dapat memenuhi harapan tersebut dan membantu mengatasi masalah yang dihadapi oleh Andi.
## Objective & Requirements

### Objective
- Membuat sistem kasir self-service di supermarket Andi.
- Memastikan bahwa sistem kasir self-service tersebut dapat mencatat informasi tentang item yang dibeli oleh pelanggan, jumlah item yang dibeli, dan harga item yang dibeli.
- Memastikan bahwa sistem kasir self-service tersebut dapat digunakan oleh pelanggan yang datang dari luar kota, sehingga memudahkan pelanggan untuk berbelanja di supermarket Andi.

### Requirements
Menggunakan bahasa pemrograman Python sebagai basis dalam pembuatan project "Super Cashier".
Mengimplementasikan materi function, branching, looping, data structure serta OOP dalam pembangunan "Super Cashier".
Memanfaatkan beberapa library yang dibutuhkan dalam pembuatan "Super Cashier" seperti numpy dan pandas untuk memudahkan pengelolaan data dan menyajikan informasi yang diperlukan.

## Flowchart <br>
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/flowchart.jpg'> <br>

## Penjelasan Kode Program

- `Transaction` : Class yang berada di dalam modular Transaksi.py yang digunakan untuk mengolah list pembelian.
- `add_item(self, nama_item, jumlah_item, harga_item, harga_total)` : Fungsi yang digunakan untuk menambahkan item baru ke dalam list pembelian
- `update_item_name(self, nama_item_lama, nama_item_baru)` : Fungsi yang digunakan untuk mengubah nama item di dalam list pembelian
- `update_item_qty(self, nama_item, jumlah_item_baru)` : Fungsi yang digunakan untuk mengubah jumlah item di dalam list pembelian
- `update_item_price(self, nama_item, harga_item_baru)` : Fungsi yang digunakan untuk mengubah harga item di dalam list pembelian
- `delete_item(self, nama_item)` : Fungsi yang digunakan untuk menghapus sebuah item di dalam list pembelian
- `reset_transaction(self)` : Fungsi yang digunakan untuk menghapus semua item di dalam list pembelian
- `TambahBarang()` : Fungsi untuk menampilkan menu tambah barang
- `UbahBarang()` : Fungsi untuk menampilkan menu ubah barang
- `HapusBarang()` : Fungsi untuk menampilkan menu hapus barang
- `CekValid()` : Fungsi untuk mengecek apakah list pembelian valid apa tidak
- `CekPembelian()` : Fungsi untuk menu cek pembelian


## Test Case
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/Test0.png'> <br>
### Test Case 1
Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut:

Nama Item: Ayam Goreng Kremes, Qty: 2, Harga: 20000 dan Pasta Gigi close down, Qty: 3, Harga: 15000 <br>
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/Test1.png'> <br>


### Test Case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi. <br>
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/Test2.png'> <br>


### Test Case 3
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan. <br>
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/Test3.png'> <br>


### Test Case 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item- item yang dibeli. <br>
<img src='https://github.com/jemmyfebryan/Python-Pacmann-Cashier-System-Project/blob/main/img/Test4.png'> <br>



## Kesimpulan
Ini adalah deskripsi proyek Python yang tersedia di repository github: "Proyek ini bertujuan untuk membantu Andi dalam mengelola transaksi pembelian barang di supermarket miliknya. Dalam proyek ini, terdapat sebuah class Transaksi yang menyediakan beberapa method seperti add_item, update_item_name, update_item_qty, update_item_price, delete_item, reset_transaction, check_order, dan total_price. Method-method tersebut berperan dalam menambah, mengubah, menghapus item, memeriksa pesanan, serta menghitung total harga dan diskon yang diberikan. Dengan proyek ini, Andi dapat mempercepat proses transaksi dan meningkatkan efisiensi manajemen supermarketnya."
