import timeit
from random import randint


def counting_sort(dizi):
	bouyut = len(dizi)
	siralanmis_dizi = [0] * bouyut
	count = [0] * bouyut
	
	for i in range(0, bouyut):
	  for j in range(i + 1, bouyut):
	    if(dizi[i] < dizi[j]):
	      count[j] += 1
	    else:
	      count[i] += 1
	
	for i in range(0, bouyut):
	  siralanmis_dizi[count[i]] = dizi[i]

	return siralanmis_dizi


def fonksiyon():
	f = open("config.txt", "r")
	adet = f.readlines()
	uzunluk = int(adet[0])
	dizi= [randint(0, uzunluk) for _ in range(uzunluk)]
	counting_sort(dizi)


def main():
	sure = timeit.timeit(fonksiyon, number=1)
	print("Counting Süre: ", round(sure, 7), "saniye.")


if __name__ == '__main__':
	main()