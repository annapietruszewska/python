vowels = ['a','e','i','o','u']
word = raw_input("Podaj slowo w ktorym bede szukac samoglowski: ")
found  = {}


for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k, 'znaleziono', v, 'razy')


""" 
fruits = {}
fruits['jablka'] = 10
print('jablka' in fruits)
if 'banany' in fruits:
    fruits['banany'] += 1
else:
    fruits['banany'] = 1
print(fruits)
if 'gruszki' not in fruits:
    fruits['gruszki'] = 0 #keyerror to blad inicjalizacji, gdy nie ma wczesniej zdefiniowanej wartosci
else:
    fruits['gruszki'] +=1
print(fruits)


fruits.setdefault('gruszki',0)
fruits['gruszki'] +=1
print(fruits)
"""
