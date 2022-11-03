import timeit
from random import randint


def partition(dizi, left, right):
    pivot = dizi[right]
    j = left
    for i in range(left, right):
        if dizi[i] <= pivot:
            dizi[i], dizi[j] = dizi[j], dizi[i]
            j += 1
    dizi[right], dizi[j] = dizi[j], dizi[right]
    return j


def quickSort(dizi, left, right, sayac):
    if left < right:
        sayac += 1

        mainstay = partition(dizi, left, right)
        dizi, sayac = quickSort(dizi, left, mainstay - 1, sayac)
        dizi, sayac = quickSort(dizi, mainstay + 1, right, sayac)

    return dizi, sayac


def fonksiyon():
    sayac = 0
    f = open("config.txt", "r")
    satirlar = f.readlines()
    adet = satirlar[0]
    uzunluk = int(adet)
    dizi = [randint(0, uzunluk) for _ in range(uzunluk)]

    dizi, sayac = quickSort(dizi, 0, uzunluk - 1, sayac)


def main():
    elapsedTime = timeit.timeit(fonksiyon, number=1)
    print("Quick Süre: ", round(elapsedTime, 7), "saniye")


if __name__ == '__main__':
	main()