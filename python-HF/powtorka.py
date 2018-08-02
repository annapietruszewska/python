from datetime import datetime
import random
import time
odds = [1,3,5,7,9,11,13,15,17,19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,53,55,57,59]

for cokolwiek in range(5):
    right_this_time = datetime.today().minute
    if right_this_time in odds:
        print("Ta minuta jest nieparzysta")
    else:
        print("ta minuta jest parzysta")
    wait_time = random.randint(1,60) #jezeli nie wetne tego bloku to on sie wykona poza petla
    time.sleep(wait_time)

from os import getcwd
where_am_I = getcwd()
print where_am_I

today = "Niedziela"
condition = "Bol glowy"

if today == "Sobota":
    print ("Impreza")
elif today == "Niedziela":
    if condition == "Bol glowy":
        print ("wpierw odpoczynek pozniej rekonwalescencja")
    else:
        print ("odpoczynek")
else:
    print ("praca, praca, praca")

#######
#beersong
#######

word = "butelki"
for beer_num in range(99,0,-1):
    print(beer_num, word, "piwa na scianie")
    print (beer_num, word, "piwa")
    print("wez jedna")
    print("podaj w kolo")
    if (beer_num == 1):
        print ("nie ma juz butelek piwa na scianie")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word ="butelka"
        print(new_num, word, "piwa na scianie")
    print()
