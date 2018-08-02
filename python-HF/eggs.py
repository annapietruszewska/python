#ten kod modyfikuje liste, przeksztalca ja, oryginalny stan listy przestaje
#byc dostepny dla mojego programu, trace poczatkowe dane
#zadna z ponizszych metod nie jest lepsza od drugiej, trzeba sie zastanowic
#co chcemy osiagnac decydujac sie na ktoras z nich
phrase = "podaj jajko"
plist = list(phrase) #list przetwarza dane z phrase i wyswietla jako liste
print(phrase)
print(plist)

for i in range(3):#precyzyjnie okresla ilosc powtorzen danej czynnosci
    plist.pop()

plist.pop(0)#new_phrase = plist.pop(0) nie musze przypisywac do tymczasowej zmiennej plist.pop(0)
plist.remove("a")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))#wyciągamy najpierw, przypisujemy pozniej

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
"""

########################
#notacja nawiasów kwadratowych
########################
#ten kod nie modyfikuje listy plist, wycinamy fragmenty listy, ale oryginalne dane
#sa nienaruszone

phrase = "podaj jajko"
plist = list(phrase) #list przetwarza dane z phrase i wyswietla jako liste
print(phrase)
print(plist)

cos = plist[5:9:1]
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join(cos)

print(plist)
print(new_phrase)"""
