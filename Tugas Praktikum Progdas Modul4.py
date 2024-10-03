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

def Jumlah(Masukan2):
    while Masukan2 <= 0:
        Masukan2 = int(input("Input anda tidak boleh nol atau minus: "))
    
    Total_Bayar = Masukan2 * Penyimpanan[Hitung]
    Perlu_bayar.append(Total_Bayar)
    print("Oke, karena anda mau pesan", Masukan2, ", jadi totalnya", Total_Bayar, "\n")

Masukan2 = int(input("Anda mau pesan berapa? (Minimal 1): "))
Jumlah(Masukan2)

def Pesanan_Tambahan(Masukan3):
    global Hitung

    if Masukan3 == "yes":
        while Hitung <= 5:
            Hitung += 1

            Percobaan.Menu_Makanan()
            
            Masukan = int(input("Silahkan dipesan ya! (1-4): "))
            hasil(Masukan)
            
            Masukan2 = int(input("Anda mau pesan berapa? (Minimal 1): "))
            Jumlah(Masukan2)

            Masukan3 = str(input("Apakah ada tambahan lagi? (yes/no): "))
            if Masukan3 != "yes":
                break
    elif Masukan3 == "no":
        pass
    else:
        Masukan3 = str(input("Mohon hanya masukan input (yes/no): "))
        Pesanan_Tambahan(Masukan3)

Masukan3 = str(input("Apakah ada tambahan lagi? (yes/no): "))
Pesanan_Tambahan(Masukan3)
