import timeit
from random import randint


def selection_sort(dizi):
    sayac = 0
    uzunluk = len(dizi)
    for i in range(0, uzunluk - 1):
        j = i
        for index in range(i + 1, uzunluk):
            if dizi[index] < dizi[j]:
                j = index
        dizi[j], dizi[i] = dizi[i], dizi[j]

        sayac += 1

    return dizi, sayac


def fonksiyon():
    f = open("config.txt", "r")
    satirlar = f.readlines()
    adet = satirlar[0]
    uzunluk = int(adet)
    dizi = [randint(0, uzunluk) for _ in range(uzunluk)]

    dizi, sayac = selection_sort(dizi)


def main():
    sureolc = timeit.timeit(fonksiyon, number=1)
    print("Selection Süre: ", round(sureolc, 7), "saniye")


if __name__ == '__main__':
	main()
