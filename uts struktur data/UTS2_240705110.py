print("==============================================")
print("              RUMAH MAKAN NYANYAK             ")
print("==============================================")
print("                  Daftar Menu                 ")
print("==============================================")
print(" Paket 1 = Nasi sie reuboh + Es teh")
print(" Paket 2 = Nasi Keumamah + Es kosong")
print(" Paket 3 = Nasi soto ayam + Sirup ABC ")
print("==============================================")
print()
# Program Antrian Restoran (Queue Pengunjung Kafe)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def tampilkan(self):
        if self.is_empty():
            print("Tidak ada kostumer yang menunggu.")
        else:
            print("Kostumer yang sedang menunggu:", end=" ")
            for item in self.items:
                print(item, end=" ")
            print()


# Program utama
antrian = Queue()
pesanan_selesai = []  # Menyimpan nama dan pesanan pelanggan

jumlah = int(input("Masukkan jumlah kostumer hari ini = "))

# Input data pelanggan
for i in range(1, jumlah + 1):
    nama = input(f"Kostumer {i} = ")
    antrian.enqueue(nama)

#meanmpilkan informasi antrian awal
print("\n===== Daftar antrian kostumer =====")
antrian.tampilkan()

# Simulasi pelayanan pelanggan
while not antrian.is_empty():
    keluar = antrian.dequeue()
    print(f"\n========  Atas Nama {keluar}   ========")
    pesanan = input("Paket yang diorder: ")
    print(f"Pesanan atas nama {keluar}: {pesanan}.")
    pesanan_selesai.append((keluar, pesanan))

    # Tampilkan sisa antrian
    print("\n=== Sisa kostumer yang menunggu ===")
    antrian.tampilkan()

# Setelah semua selesai menampilkan semua kostumer yang dilayani hari ini
print("\n===== Daftar Pesanan Hari Ini =====")
for nama, pesanan in pesanan_selesai:
    print(f"{nama} - {pesanan}")

print("\nSemua kostumer sudah dilayani. Terima kasih telah berkunjung!")
print("                      JAK JAK LOM BEH!                         ")
print()