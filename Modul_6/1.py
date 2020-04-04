print("\nNomor 1")
class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

a0 = Mahasiswa('Ika', 10, 'Sukoharjo', 240000)
a1 = Mahasiswa('Budi', 51, 'Sragen', 230000)
a2 = Mahasiswa('Ahmad', 2, 'Surakarta', 250000)
a3 = Mahasiswa('Chandra', 18, 'Surakarta', 235000)
a4 = Mahasiswa('Eka', 4, 'Boyolali', 240000)
a5 = Mahasiswa('Fandi', 31, 'Salatiga', 250000)
a6 = Mahasiswa('Deni', 13, 'Klaten', 245000)
a7 = Mahasiswa('Galuh', 5, 'Wonogiri', 245000)
a8 = Mahasiswa('Janto', 23, 'Klaten', 245000)
a9 = Mahasiswa('Hasan', 64, 'Karanganyar', 270000)
a10 = Mahasiswa('Khalid', 29, 'Purwodadi', 230000)

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

def urutkanNIM(a):
    baru = {}
    for i in range(len(a)):
        baru[a[i].nama] = a[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elem in listofTuples:
        print (elem[0], ':', elem[1])

urutkanNIM(Daftar)

