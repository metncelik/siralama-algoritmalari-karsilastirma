import timeit
from random import randint


def insertion_sort(dizi):
	sayac = 0
	uzunluk = len(dizi)
	for i in range(0, uzunluk):
		value = dizi[i]
		j = i
		while (j > 0) and (dizi[j - 1] > value):
			dizi[j] = dizi[j - 1]
			j -= 1
		dizi[j] = value

		sayac += 1

	return dizi, sayac


def fonksiyon():
	f = open("config.txt", "r")
	adet = f.readlines()
	uzunluk = int(adet[0])
	dizi = [randint(0, uzunluk) for _ in range(uzunluk)]

	dizi, sayac = insertion_sort(dizi)


def main():
	sureolc = timeit.timeit(fonksiyon, number=1)
	print("Insertion Süre: ", round(sureolc, 7), "saniye")


if __name__ == '__main__':
	main()
