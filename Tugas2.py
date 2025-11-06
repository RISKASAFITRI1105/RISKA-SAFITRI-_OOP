# === Data Dosen ===
class Dosen:
    def __init__(self, nama, usia, nidn, mata_kuliah):
        self.nama = nama
        self.usia = usia
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"{self.nama} sedang mengajar {self.mata_kuliah}.")


# === Data Mahasiswa ===
class Mahasiswa:
    def __init__(self, nama, usia, nim, jurusan):
        self.nama = nama
        self.usia = usia
        self.nim = nim
        self.jurusan = jurusan

    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan {self.jurusan}.")


# Membuat objek dosen
dosen1 = Dosen("Edy", 17, 123456, "Pemrograman Berorientasi Objek")
print("=== Data Dosen ===")
print(f"Nama: {dosen1.nama}")
print(f"Usia: {dosen1.usia}")
print(f"NIDN: {dosen1.nidn}")
print(f"Mata Kuliah: {dosen1.mata_kuliah}")
dosen1.mengajar()

print("\n=== Data Mahasiswa ===")
mahasiswa1 = Mahasiswa("Riska Safitri", 20, "24241173", "Pendidikan Teknologi Informasi")
print(f"Nama: {mahasiswa1.nama}")
print(f"Usia: {mahasiswa1.usia}")
print(f"NIM: {mahasiswa1.nim}")
print(f"Jurusan: {mahasiswa1.jurusan}")
mahasiswa1.belajar()


# === Pewarisan Kelas (Inheritance) ===
class Binatang:
    def __init__(self, nama):
        self.nama = nama
        self.hidup = True

    def makan(self):
        print(f"{self.nama} sedang makan")

    def tidur(self):
        print(f"{self.nama} sedang tidur")


class Kambing(Binatang):
    def suara(self):
        print("mbeeek")


class Babi(Binatang):
    def suara(self):
        print("nggook")


class Ular(Binatang):
    def suara(self):
        print("sssstttt")


# Membuat objek dari tiap kelas turunan
kambing = Kambing("Rizky")
babi = Babi("Koruptor")
ular = Ular("Fariz")

print("\n=== Aktivitas Binatang ===")
print(ular.nama)
print(ular.hidup)
ular.makan()
ular.tidur()
ular.suara()  # Memanggil suara dari objek ular
