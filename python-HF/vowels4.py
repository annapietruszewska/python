"""
vowels = ['a','e','i','o','u']
word = raw_input("Podaj wyraz: ")

found = {}

found['a'] = 0#nie mozemy tego usunac bo klucze slownika musza byc zainicjalizowane
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k, 'znaleziono', v, 'razy')
"""

fruits = {}
fruits['jablka'] = 10
print(fruits)

if 'banany' in fruits:
    fruits['banany'] += 1
else:
    fruits['banany'] = 1
print(fruits)

if 'gruszki' not in fruits:
    fruits['gruszki'] = 0
fruits['gruszki'] += 1
print(fruits)

        
