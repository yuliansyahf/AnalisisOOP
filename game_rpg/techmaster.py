from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def get_harga(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self, nama, harga, processor):
        super().__init__(nama, harga)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga() * 0.10
        return (self.get_harga() + pajak) * jumlah


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga, kamera):
        super().__init__(nama, harga)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga() * 0.05
        return (self.get_harga() + pajak) * jumlah


def proses_transaksi(daftar):
    total = 0
    for barang, jumlah in daftar:
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f"Beli {jumlah} unit | Subtotal: Rp {subtotal:,}")
        total += subtotal
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total:,}")


# -- MAIN --
print("--- SETUP DATA ---")
laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

print("\n--- STRUK TRANSAKSI ---")
proses_transaksi([
    (laptop, 2),
    (hp, 1)
])
