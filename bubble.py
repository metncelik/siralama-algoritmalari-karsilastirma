import timeit
from random import randint


def bubble_sort(dizi):
	sayac = 0
	uzunluk = len(dizi)
	for i in range(0, uzunluk - 1):
		is_sorted = True
		for j in range(0, uzunluk - 1):
			if dizi[j] > dizi[j + 1]:
				dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
				is_sorted = False
		sayac += 1
		if is_sorted:
			break

	return dizi, sayac


def fonksiyon():
	f = open("config.txt", "r")
	adet = f.readlines()
	uzunluk = int(adet[0])
	dizi= [randint(0, uzunluk) for _ in range(uzunluk)]
	dizi, sayac = bubble_sort(dizi)


def main():
	sure = timeit.timeit(fonksiyon, number=1)
	print("Bubble Süre: ", round(sure, 7), "saniye.")


if __name__ == '__main__':
	main()
