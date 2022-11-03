import counting
import insertion
import quick
import selection
import bubble

f = open("config.txt", "w")
s= input("Sayi adeti:")
f.write(s)
f.close()

bubble.main()
counting.main()
insertion.main()
quick.main()
selection.main()