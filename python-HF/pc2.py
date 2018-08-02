from string import maketrans
abc = "abcdefghijklmnopqrstuvwxyz"
trans = "cdefghijklmnopqrstuvwxyzab"
w = maketrans(abc,trans)
str = "map"
print str.translate(w)


    
    






