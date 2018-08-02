# -*- coding: utf-8 -*-
#############
#Program odd.py
#############
print "Program odd.py:"

from datetime import datetime #możemy importować submoduł lub funkcję
import random
import time
#przypisanie do zmiennej odds listy liczb calkowitych
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("Ta minuta wydaje sie dosc nieparzysta.") #wcięcie jedyny mechanizm grupowania kodu
    else:
        print("Minuta parzysta.") #wcięty zestaw(blok) poprzedzony :
    wait_time = random.randint(1,30) #randint generuje liczbe losowa z przedzialu, jeżeli nie zrobię wcięcia w tym bloku to random i sleep się nie wykonają
    time.sleep(wait_time)

#zmienna tymczasowa
time_now = datetime.today()
right_this_time = time_now.minute

#############
#Importowanie modulu i wywolanie funkcji
#############
print "\nimport modulu os:"

from os import getcwd

where_am_I = getcwd()
print where_am_I

#############
#wywołanie funkcji today() i odwolanie się do jej atrybutu minute
#############
print "\nprzyklad z ksiazki na biezaco:"

from datetime import datetime

right_this_minute = datetime.today().minute

print right_this_minute

#############
#Else, Elif - instrukcja warunkowa
#############
#else obsługuje wszystkie pozostałe przypadki

print "Instrukcje warunkowe elif else"

today = 'Niedziela'
condition = 'Bol glow'
if today == 'Sobota':
    print ('Impreza!')
elif today == 'Niedziela':
    if condition == 'Bol glowy':
        print ('rekonwalescencja, potem odpoczynek')
    else:
        print ('odpoczynek')
else:
    print ('Praca, praca, praca')

#############
#wyświetlanie opisu/pomocy
#############

#>>>dir(random)
#>>>help(random.randit)

#############
#beersong
#############

print 'Beersong'

word = "butelki"
for beer_num in range(99,0,-1): #beer_num zmienna iteracyjna petli
    print (beer_num, word, "piwa na scianie")
    print (beer_num, word, "piwa")
    print ("wez jedna")
    print ("podaj w kolo")
    if beer_num == 1:
        print ("Nie ma juz butelek piwa na scianie")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "butelka"
        print (new_num, word, "piwa na scianie")
    print() #wyswietl pusty wiersz
