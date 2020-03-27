class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("diah", 12, "Sragen", 240000)
c1 = MhsTif("siwi", 41, "Tegal", 230000)
c2 = MhsTif("amanda", 8, "Surakarta", 250000)
c3 = MhsTif("Chandra", 17, "Magelang", 235000)
c4 = MhsTif("brian", 62, "Boyolali", 240000)
c5 = MhsTif("nisa", 51, "Salatiga", 250000)
c6 = MhsTif("fandi", 15, "Klaten", 245000)
c7 = MhsTif("fauzi", 64, "Wonogiri", 245000)
c8 = MhsTif("putri", 43, "Klaten", 245000)
c9 = MhsTif("nimas", 74, "Karanganyar", 270000)
c10 = MhsTif("viola", 24, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def temp(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp
    
def urutNim(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                temp(a,y,y+1)

def cekNim(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.kotaTinggal)


