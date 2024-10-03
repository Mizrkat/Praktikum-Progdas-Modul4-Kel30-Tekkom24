from Method import Percobaan

Harga_Makanan = {
    1: (15000, "Nasi goreng"),
    2: (7000, "Mie goreng"),
    3: (10000, "Mie rebus"),
    4: (20000, "Nasi ayam")
}

Tambahan_biaya = {
    1: (0, "COD"),
    2: (1000, "QRIS"),
    3: (2000, "Transfer bank")
}

Penyimpanan = []
Perlu_bayar = []
Hitung = 0

Percobaan.Menu_Makanan()

def hasil(Masukan):
    while Masukan >= 5 or Masukan <= 0:
        Masukan = int(input("Input anda salah, pilih antara (1-4) ya!: "))

    Harga, Makanan = Harga_Makanan[Masukan]
    print("karena anda memilih", Makanan, ", harganya adalah {}\n".format(Harga))
    Penyimpanan.append(Harga)

Masukan = int(input("Silahkan dipesan ya! (1-4): "))
hasil(Masukan)
