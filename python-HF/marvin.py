"""
paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print'\t',char#w pythonie wyglada to tak: print('/t',char)
"""

#################
#wersja programu operujaca na wycinkach
#################

paranoid_android = "Marvin, panaroiczny android"
letters = list(paranoid_android)
for char in letters[:6]:
    print'\t',char
print()

for char in letters[-7:]:
    print'\t'*2,char
print()

for char in letters[8:19]:
    print'\t'*3,char
print()
