print("========================================")
print("              DATA KONSUMEN             ")
print("========================================")


# Program Queue Konsumen (Nomor 1 - Semua keluar antrian)

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
            print("(kosong)")
        else:
            for item in self.items:
                print(item, end=" ")
            print()


# Program utama
antrian = Queue()

jumlah = int(input("Masukkan jumlah konsumen = "))

# Input data konsumen
for i in range(1, jumlah + 1):
    nama = input(f"Konsumen {i} = ")
    antrian.enqueue(nama)

# Cetak semua data awal
print("Cetak List =", end=" ")
antrian.tampilkan()
print()

# Simulasi: keluarkan satu per satu
while not antrian.is_empty():
    keluar = antrian.dequeue()
    print("Memanggil Konsumen =", keluar)

    print("Cetak List =", end=" ")
    antrian.tampilkan()

    print()
    