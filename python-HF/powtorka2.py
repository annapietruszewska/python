"""
vowels = ['a', 'e', 'i','o','u']
word = raw_input("podaj slowo")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(found)#wyswietla tablice
for i in found:
    print(i)


phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)

plist.remove('a')
plist.extend([plist.pop(),plist.pop()])#zamienia miejscami ostatnie litery
plist.insert(2,plist.pop(3))#przeuwa spacje o jedno miejsce w bok

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3:1]+ plist[5:9:1])

print(plist)
print(new_phrase)


"""

p_a = "Marvin, paranoiczny android"
let = list(p_a)
for char in let[:6]:
    print '\t', char
print()
for char in let[-7:]:
    print '\t'*2, char
print()
for char in let[8:19]:
    print'\t'*3, char
print()
    
