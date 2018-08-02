# -*- coding: utf-8 -*-
#############
#Program odd.py
#############
print "Program odd2.py:"

from datetime import datetime #1 sposób: możemy importować submoduł lub funkcję
import random #2 sposob: importujemy modul
from time import sleep
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
    wait_time = random.randint(1,60) 
    sleep(wait_time) #mozemy tutaj napisac time.sleep(wait_time) ale wtedy na gorze robimy tylko import time




