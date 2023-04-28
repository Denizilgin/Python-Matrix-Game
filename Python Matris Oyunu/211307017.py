import sys
import random


with open(sys.argv[1], 'r') as f:
    content = f.read().rstrip()

lines = content.split('\n')
matris = []

for line in lines:
    row = line.split()
    matris.append([int(x) for x in row])

for row in matris:
    for element in row:
        print(element, end=' ')
    print(end='\n')
print("-"*10 + " OYUN BAŞLADI İYİ OYUNLAR " + "-" * 10)

def fibonacci(sayi):
    if sayi == 0:
        return 0
    elif sayi == 1:
        return 1
    else:
        return fibonacci(sayi-1) + fibonacci(sayi-2)

def puan_hesaplama(deger, say):
    return fibonacci(say + 1) * deger

with open(sys.argv[1], 'w') as dosya:
    for satir in matris:
        dosya.write(' '.join(map(str, satir)) + '\n')

def matris_oku(dosya_adi):
    with open(dosya_adi, 'r') as dosya:
        lines = dosya.readlines()
        matris = []
        for line in lines:
            satir = list(map(int, line.strip().split()))
            matris.append(satir)
        return matris

def matris_yazdirma(matris):
    for satir in matris:
        for num in satir:
            print(num, end=' ')
        print()


def komsu_bulma(matris, satir, sutun, deger):
    komsular = []
    komsulari = set()
    def koms_2(sat, sut):
        if (sat, sut) in komsulari or sat < 0 or sat >= len(matris) or sut < 0 or sut >= len(matris[0]) or matris[sat][sut] != deger:
            return
        komsulari.add((sat, sut))
        komsular.append((sat, sut))
        koms_2(sat-1, sut)
        koms_2(sat+1,sut)
        koms_2(sat, sut-1)
        koms_2(sat, sut+1)
    koms_2(satir, sutun)
    return komsular

def hucre_silme(matris, hucreler):
        satirlar, sutunlar = len(matris), len(matris[0])
        for satir, sutun in hucreler:
            matris[satir][sutun] = ' '

        for c in range(sutunlar):
            bos_hucre = satirlar - 1
            for r in range(satirlar - 1, -1, -1):
                if matris[r][c] == ' ':
                    continue
                if bos_hucre != r:
                    matris[bos_hucre][c] = matris[r][c]
                    matris[r][c] = ' '
                bos_hucre -= 1


def oyun(matris):
    puan = 0
    satirlar = len(matris)
    sutunlar = len(matris[0])
    while True:
        matris_yazdirma(matris)
        print("Puan ---> ", puan)
        satir = int(input("Satir giriniz: ")) - 1
        sutun = int(input("Sutun giriniz: ")) - 1
        if satir < 0 or satir >= satirlar or sutun < 0 or sutun >= sutunlar:
            print("-" * 15)
            print("Lütfen geçerli hücre girin.")
        elif matris[satir][sutun] == ' ':
            print("-" * 15)
            print("Hücre zaten silindi.")
        else:
            deger = matris[satir][sutun]
            komsular = komsu_bulma(matris, satir, sutun, deger)
            if not komsular:
                print("Oyun Bitti.")
                with open(sys.argv[2], "w") as file:
                    for row in matris:
                        line = " ".join(str(num) for num in row)
                        file.write(line + "\n")
                break
            else:
                sayac = len(komsular)
                points = puan_hesaplama(deger, sayac)
                puan += points
                hucre_silme(matris, komsular)
                with open(sys.argv[2], "w") as file:
                    for row in matris:
                        line = " ".join(str(num) for num in row)
                        file.write(line + "\n")





matris = matris_oku(sys.argv[1])
oyun(matris)