from math import sqrt
for n in range(1, 26): #in this statement we set instructions for n in a range for (1,26)
    r = 2.0 # r variable eqauals 2.0
    for i in range(n):
        r = sqrt(r) # in this statement r now eqausl the square root of r
    for i in range(n):
        r = r**2 #in this statment r is squared


    print r
