# Nama  : Riska Safitri
# Nim   : 24241173
# Program: Class Mobil


class Mobil:
    def __init__(self, merk, model, warna, cc, kondisi_mesin, surat_surat, harga):
        self.merk = merk
        self.model = model
        self.warna = warna
        self.cc = cc
        self.kondisi_mesin = kondisi_mesin
        self.surat_surat = surat_surat
        self.harga = harga

    def info_mobil(self):
        print(f"Merk            : {self.merk}")
        print(f"Model           : {self.model}")
        print(f"Warna           : {self.warna}")
        print(f"CC              : {self.cc} cc")
        print(f"Kondisi Mesin   : {self.kondisi_mesin}")
        print(f"Surat-surat     : {self.surat_surat}")
        print(f"Harga           : Rp{self.harga:,}")

# Membuat objek mobil dengan data yang berbeda
mobil_baru = Mobil(
    merk="Toyota",
    model="Fortuner",
    warna="Hitam",
    cc=2800,
    kondisi_mesin="Sangat Baik",
    surat_surat="Lengkap (STNK & BPKB)",
    harga=750000000
)

mobil_baru.info_mobil()

