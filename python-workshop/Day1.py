# -*- coding: utf-8 -*-
# single comment

""" multiple comma
"""

#######
# data types tak rozdzielamy zagadnienia, to sa bloki 
######

a = 1#integer
print type(a)
a = "1"#string
print type(a)
a = 1.0#flow
print type(a)

#######
# tuple pierwszy typ danych, krotka rozne typy danych, indeksowanie od 1
######

a = (1,2,3,4,5)
print type(a)
print a[0]
print a[1]
print a[2]
print a[3]
print a[4]

#nei mozemy zmodyfikowac tupla jest niemodyfikowalna
#a[0]=6

a = 1,2,3,4,5
print type(a)

a = 1
b = 2
#PODMIANA WARTOSCI nei musimy zapisywac do zmiennej zeby podmienic inne wartosci

a,b=b,a

print a
print b

#tworzenie krotki, wbudowana funkcja tuple

a = tuple()
print type(a)


#####
#LISTY modyfikowalne sa podnieniamy, zamieniamy
######

a = [1,2,3,4,5]

print a[0]
print a[1]
print a[2]
print a[3]
print a[4]

print a

a.append(6) #dodawanie do listy kolejnej liczby na koncu, append metoda
#jest wykonywana na rzecz obiektu a funkcja nie

print a

#print dir(a) # pozwala wyswietlac metody

a.insert(0,7) #index, Value do zerowej pozycji dodajemy cyfre 7

print a

#usuwanie z listy elementow spod danego indexu

del a[0] # jako argument podajemy index
del a[5]
print a

#petla for each, dla kazdego elemtnu w kolecji, wciecia to sa 4 spacje,
#opcje widnow opcjons, configure mozna zmienic ilosc spacji
print "jestem tutaj"
for elem in a:
    print elem

#towrzenie listy, dostajemy liste od do 1 do 9 bez 10
a = range(1,10)
print a

#petla klasyczna for ktora idzie 10x to musimy zrobic zawsze z rangem
for elem in range(1,11):
    print elem
#comprehension list, skladanie list, udowa listy na podstawie istniejacej
a = [x for x in range(1,10)]
print a

a=[1,2,3,4,5]
new_list  = []
for elem in a:
    new_list.append(elem*2)
    print new_list

#to samo za pomoca comprehension
a = [x*2 for x in a]
print a

#######
#slices, krojenie elementow indeksowanlnych
#####
a = "sample tekst"
print a
b = [1,2,3,4,"a"]
c = (1,2,3,4,5)
print a[0:3:1] #<)
print b[0:3:1] #<)
print c[0:3:1] #<)

print a[len(a) - 1]
print b[len(b) - 1]
print c[len(c) - 1]

print a[-1] # ostatni element wyswietl
print b[-1]
print c[-1]

print a[-1:-4:-1] #w lewo krok -1 bez -4

#slices do odwracania tekstu
#the qick brown fox, zawiera wszystkie angielskie litery?!
a = "sample"
print a
print a[::-1] #odwracanie ciagu tekstowego, bez -1 to bedziemy meic liste
print a [::]

#######
#set
#####

#cos jak lista tylko elementy sie nie moga powtarzac, duplikaty eleminujemy, nie mamay indeksow

a=[1,2,3,4,5]
b = "sample"

aSet = set(a)
bSet = set(b)

print aSet
print bSet# bez uporzadkowania tylko sprawdza elementy

print 2 in aSet
print "b" in bSet# in sprawdza czy element jest w zbiorze

#jezeli chcemy dodac do zbioru jakis element

aSet.add(10) 
print aSet

#krotke dodajemy do zbioru ktora sklada sie z 2 elementow

b = (1,2)
aSet.add(b)

print aSet

#dodajemy liste

#c = [1,2]
#aSet.add(c)
#print aSet #dodajemy liste, ale wyskakuje blad bo lista nie moze byc elementem zbioru
#set contains only immutalbe elements , to co wyzej z bledem
# usuwanie ze zbioru konkretny element
aSet.remove(10)
print aSet

a = (1,2,3,4,5)#z krotki nei mozemy usuwac bo jest niemutowalne
print type(a)

######
#slowniki, dictionary, mapy, slowniki to sa javove mapy, klucz wartosc
######
numbers ={
  "a":1,
  "b":2,
  "c":3
    }
print numbers

print numbers["a"]
print numbers["b"]
print numbers["c"]

print numbers.keys()
print numbers.values()
print numbers.items()

#dodawanie elementu do slownika
#numbers["d"] = 4
#print numbers
#usuwanie 
#del numbers["d"]

######
#syntax skladnia
#####

if 1<2:
    pass
elif 1<3:
    pass
else:
    pass
a = "sample"
print a
print a.index("p")
print 10* "2"
a = 1
b = "1"
print str(a)
print int(b)

#help(str)
#dziala tylko w pythonie w wersji 2, do dodawania komentarzy
print a,"to jest zmienna a"
print ("sample") #w wersji 3pythona
print "sample"



#potega a ** b

#szyfr cezara, ptython challange

print ord ("a")
print chr(97)

#instalowanie wlasnych modulow
#otwieramy cmdline, django

#interpertuje stringa jako kod do wykonania
print eval("2+2")
#####
#ex1
######


text = "Ala ma kota"
print text
a = text.split()
print a
b = a[::-1]
print b
print " ".join(b)
print " ".join(text.split()[::-1])


####
#ex2
#tupla lista zbiory slowniki. lista vs zbior nie ma indeksowania
#czy mozna sie przeliterowac po kropce i ciagu tekstowego, replace - robi nowy ciag tekstowy od nowa na podstawie istniejacego. krotke tworzymy na 3 sposoby () lub przecinki, liste tworzymy za pomoca [], range i comprehension list, comprehension list jest po to zeby mniej kodu pisac i wydajnosc kodu, zbiory dodajemy add i remove, a tupe zbioru mozemy zrobic, lista nie moze  byc kluczem w slowniku, musi to byc element neimutowalny
#items zwraca liste tupli
#####

numbers = {
    "abc": 2,
    "def": 3,
    "ghi": 4,
    "jkl": 5,
    "mno": 6,
    "prs": 7,
    "tuw": 8,
    "xyz": 9
    }
print numbers
print 3 * "3"
#ala ma kota
#25552#62#5566682
#print raw_input ('napisz cos')
#x = raw_input

#text = "ala"
#a = list(text)

#print a
#wyswietla mi jedno pod drugim
#for letter in a:
 #   print numbers.value
    


#b = a[::]
#print b


numbers = {
    "abc":2,
    "def":3
    }
text = "ae".lower()
result = ""
for letter in text: #litery izdie po literach
    for item in numbers.items(): 
        if letter in item[0]:
            index = item[0].index(letter) + 1 #dodajemy 1 bo indeksowanie jest od zera
            print index
            print item
            result += index * str(item[1]) #konkatenacja czyli 2*"22"
print result

#break w tym programie mozna zastosowac w momencie

####
#ex3, zamieniamy na string, definiujemy zbior i srawdzamy ile jest unikalnych cyfr
####

a = 177
#a = raw_input("podaj lizcbe")#zawsze w postaci stringa, w 3ciej wersji jest tylko input
b = set (str (a))
print len(b) #sprawdzanie

#do zbioru nie mozna dodac listy
#kluczem w slowniku nie moze byc lista, tylko immutable wartosci

#####
#ex4
####



import random
x = random.randint(1,6)
print "wynik x:"
print x
y = random.randint(1,6)
print "wynik y:"
print y

#if x=y:
 #   print li.append ():

#pair = tuple()
#pair_eq = []
#pair_smal= []
#pair_other = []

#for x in range (1,7):
#    for y in range (1,7):
#        if x==y:
#        pair_eq.append(pair)
#        pass
#    elif x<y:
 #       pair_smal.append(pair)
#        pass
 #   else:
 #       pair_other.append(pair)
 #       pass
#print pair_eq
#x=0
#y=0
#for elem in pair_eq:
#    x+=elem[0]
#    y+=elem[1]
#
#print x,y "x is equal to y"

#x=0
#y=0
#for elem in pair_smal:
 #   x+=elem[0]
  #  y+=elem[1]
  #  print x,y "x is smaller than y"

#x = 0
#y = 0
#for elem in pair_other:
#    x+=elem [0]
#    y+=elem[1]
#    print x,y "other parameters"

####
#ex5
###

#text = "anna".lower()

#print text[::-1].replace(" "," ") == text.replace(" "," ")

#co jest fałszem w pythonie wszystko co jest puste

#if 0
#print"ok"
#if ():
#    print"ok"
#if [0]:
#    print "ok"

#jutro funkcje, lambdy, funkcje anonimowe
#3ci dzien - klasy

####
#ex6 - powtorka
####


#a = 21
#b = 15

#print int (str (a)[::-1]) +int(str(b)[::-1])[::-1]
####
#funckje
####


def fun(arg):
    return arg
print fun(10)
def fun(arg, a= 10):
    return arg, a
print fun(10,20)

def fun(*arg):
    return arg
print fun(1,2,3,4,5)
print fun(1,2,3,4)
print fun(1,2,3)

def fun (**arg):
    return arg

print fun(a =1, b=2, c=3)
print fun(a=1, b=2)
print fun(a=1)

#przynajmniej jeden parametr musi byc przekazany
def fun(a, *arg):
    return a, arg

print fun (1,15)
#print fun()



###
#lambda
####

#lambda to funckaj bez nazwy


def fun(x):
    return x*2

a=lambda x : x*2 #ekwiwalent powyzszego zapisu
print type(a)

print a(2)

a= [1,2,3,4,5,6,7,8,9,10]
def fun(list, n):
    new_list = []
    for elem in list:
        if elem > n:
            new_list.append(elem)
            return new_list
    pass
#return [4,5,6,7,8,9,10]
print fun(a,3)
#return [6,7,8,9,10]
print fun (a,5)

def fun(arg):
    if arg > 3:
        return True
    else:
        return False
print filter(fun, a)

print filter(lambda arg:True if arg > 3 else False, a)
print filter(lambda arg: arg>3,a)

a= [1,2,3,4,5,6,7,8,9,10]

help(map)
def fun(arg):
    return arg*2

print map(fun, a)

#a= [1,2,3,4,5]
#def fun (lst):
   # pass

#120
#print fun(a)

"""
1*2=2
2*3=6
6*4=24
24*5=120
"""
#print reduce(lambda x,y :x*y,a)

def filter_long_words(lst, n):
    return filter(lambda arg: True if len(arg) > n else Fake, lst)
def filter_long_words(lst, n):
    return filter(lambda arg:len(arg) > n, lst)
def maps_list_word_to_list_len(lst):
    return map(lambda arg: len(arg), lst)

print maps_list_word_to_list_len(['a','bb','ccc'])
print filter_long_words(['aaa','baa','caa','daaa','eaa'],3)

#programowanie reaktywne

def fun(arg):
    return arg
def fun2(arg):
    return arg
print fun(fun2)
print fun(fun2)(4)

####
#zad7, ile razy wystepuje dana litera
###
"""
a= "aaaaabcaaaa"
def fun(arg):
    dictionary = ()
    for letter in a:
        if letter in dictionary:
            dictionary[letter] += 1
            else:
                dictionary[letter] = 1
                return dictionary
            print fun(a)


"""
#####
            #regex
            ####

import re
text = " this is this is sample text 54 3 sample"

print re.search("s.*", text)
print re.search("s.*", text).group()
print re.match("s.*", text)#przeszukuje od poczatku

print re.match(".* is", text).group() #zeby wyswietlil co zostalo dopasowane, gwiazdka operator zachlanny, tzn greedy operator, z defaultu, gdy chcemy zeby wyszukiwanie bylo do pierwszego wystapienia
print re.match(".*? is", text).group() #? powoduje ze gwiazdka nei jest greedy


print re.match("(.*)iws sampke text(\d[2])", text).group(0) #caly ciag tekstowy
print re.match("(.*)iws sampke text(\d[2])", text).group(1)#pierwszy nawias wyswietlony
print re.match("(.*)iws sampke text(\d[2])", text).group(2)#drugi nawias wyswietlony
 #\d  oznazca ekwiawalent \d <=> [0-9]
 #[A-Z], [A-Za-z]
 #[*:]
 #[2,4]

text = "23sample05"
print re.match("[0-9][2]", text).group()
print re.findall("[0-9][2]", text)#zwraca napotkane wyniki

"""
[] przedzial od 0 do 9
() 
{} krotnosci
\w \d, 
"""

#napizs program ktory sprawdza czy nasz ciag to 9 znakow
a = ":****;;;:;"

print re.match("[:*][9]&",a).group()#^mowi o tym ze ciag ma sie zaczynac i posiadac dokladnie 9 znakow
print re.search("^[:*][9]", a).group()

#####
#I/o
####
try:
    f = open("zad7.txt")
    lines = f.readlines()
    print lines

    #f.seek(0)#comes back to the rist line in the file
except IOError as e:
print e
    else:
    f.close()
    finally:
    pass

            try:
    f = open("zad7.txt")
    lines = f.readlines()
    print lines

    f.seek(0)#comes back to the rist line in the file
   lines = f.read().splitlines()
   print lines
   
except IOError as e:
        print e
        else:
            f.close()
            finally:
                pass

            for elem in range(1,10)
            break
        else:
            print "else block"

text = 'Allowed Hello Hollow'
for m in re.finditer('ll', text):
    print ('ll found',m.start(), m.end())
            

exit()

#funkcje anonimowe lambda, filter map reduce
#najbardziej popularne funcke filter map reduce
# else przy otwieraniu pliku, with ktory automatycznie zamyka, lepiej stosowac with
#rise odpowiednik throw

#zadanie 6 powtorkowe
#zadanie z lambda też ok
#zadanie 7 match - szuka pierwzse wystapienie, search w calym ciagu tekstowym szuka, zwracany pierwszy npotkany wynik,findall - parametry zapisywae i dorzucane do listy
#zadanie 8 w czwartek - klasy, generatory i  iteratory, jak tworzymy wlasne iteratory
#przeciazanie























