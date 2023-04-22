#ZADANIE 2
zdanie = input("Napisz dowolne zdanie, a zmienię jego kolejność :) ")
podzielone_zdanie = zdanie.split(" ")
odwrocone_slowa = podzielone_zdanie[::-1]
odwrocone_zdanie = " ".join(odwrocone_slowa)
print(odwrocone_zdanie)
