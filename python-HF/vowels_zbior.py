"""vowels = ['a','e','i','o','u']
word = raw_input('Podaj slowo: ')

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)"""

vowels = set('aeiou')
word = raw_input('Podaj slowo: ')
found = vowels.intersection(set(word))
for vowels in found:
   print(vowels)
#print(found) p printuje nam zbior liter 
