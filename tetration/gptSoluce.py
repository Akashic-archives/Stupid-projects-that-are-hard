def chaineExpo(x, expo, multiAPart):
    if expo == 0:
        x = 1
    elif expo == 1:
        x = x
    elif expo % 2 == 0:
        expo = expo // 2
        x = x**2
    elif expo % 2 == 1:
        expo = (expo-1) // 2
        multiAPart = multiAPart * x
        x = x**2
    return x * multiAPart

x = 5
expo = 3125
multiAPart = 1

while expo > 1:
    x = chaineExpo(x, expo, multiAPart)
    print(x, "\n E = ", expo, "\n M = ", multiAPart, "\n x = ", x)








#import math
#import time

#seconds = time.time()

#def fast_pow(x, n):
#    if n == 0:
#        return 1
#    elif n == 1:
#        return x
#    elif n % 2 == 0:
#        print(time.time()/1.2)
#        return fast_pow(x**2, n//2)
#    else:
#        print(time.time()/1.2)
#        return x * fast_pow(x**2, n//2)

#x = 5

#for _ in range(5):  # Apply the expression 5 times
#    x = fast_pow(5, x)
#    print(x, "\n\n\n")

#print(x)











#import math
#import decimal
#import gmpy2

#x = decimal.Decimal(5)

#x = gmpy2.mpz(5)

#for _ in range(5):  # Apply the expression 5 times
    # x = math.exp(x * math.log(5)) marche avec error
#    x = x**decimal.Decimal(5)
    #x = x**5
#    print(format(x, 'f'))

#print(format(x, 'f'))
#print(str(x))
