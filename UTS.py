# Definisi Class Rumah
class Rumah:
    # Constructor untuk inisialisasi atribut rumah
    def _init_(self, pemilik, alamat, luas):
        self.pemilik = pemilik  # Nama pemilik rumah
        self.alamat = alamat    # Alamat rumah
        self.luas = luas        # Luas rumah dalam meter persegi
    
    # Method untuk menampilkan informasi rumah
    def info_rumah(self):
        return f"Pemilik: {self.pemilik}, Alamat: {self.alamat}, Luas: {self.luas} m2"

# Definisi Class Rumah Mgt_(pemilik, alamat, luas)  # Memanggil constructor dari class Rumah
        self.jumlah_kamar = jumlah_kamar  # Jumlah kamar dalam rumah mewah
    
    # Method yang di-override untuk menampilkan info rumah mewah
    def info_rumah(self):
        info_awal = super().info_rumah()  # Memanggil method info_rumah dari class induk
        return f"{info_awal}, Jumlah Kamar: {self.jumlah_kamar}"

# Membuat objek dari class Rumah
rumah_biasa = Rumah("Siti", "Jl. Kenanga No. 10", 120)

# Membuat objek dari class RumahMewah
rumah_mewah = RumahMewah("Andi", "Jl. Melati No. 20", 300, 5)

# Menampilkan informasi rumah biasa dan rumah mewah
print(rumah_biasa.info_rumah())    # Output: Pemilik: Siti, Alamat: Jl. Kenanga No. 10, Luas: 120 m2
print(rumah_mewah.info_rumah())    # Output: Pemilik: Andi, Alamat: Jl. Melati No. 20, Luas: 300 m2, Jumlah Kamar: 5