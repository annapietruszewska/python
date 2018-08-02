# -*- coding: utf-8 -*-
#########
#vowels.py - szukanie liter w slowie
#########

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Miliard"

ile = len(vowels)#funkcja len()wyswietla info o rozmiarze obiektu
print(ile)

for letter in word:
    if letter in vowels:
        print(letter)

#########
#vowels2.py - szukanie liter w slowie
#########

print('Zmieniony program vowels, rozszerzanie listy, append, operator not in')

vowels = ['a', 'e', 'i', 'o', 'u']
word = raw_input("Podaj slowo, w ktorym nalezy szukac samogloski: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

#########
#współdzielenie referencja(odwołanie) do tegj samej listy miedzy zmiennymi, to nie jest kopiowanie listy
#########
print("Referencja i kopiowanie listy")
first = [1,2,3,4,5]
print(first)
second = first# dobre w momencie jak inna zmienna ma miec dostep do listy i ja modyfikowac
print(second)
second.append(6)
print(second)
print(first)
import copy#dla zainicjowania nowej listy wybieramy copy
third = copy.copy(second)

third.append(7)
print(third)
print(second)

#########
#listy i indeksowanie
#########

saying = "Podaj jajko!"
letters = list(saying)
print(letters)
print(letters[0:10:3])
print(letters[3:])
print(letters[:10])
print(letters[::2])

