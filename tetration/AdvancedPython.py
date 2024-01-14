# methode 3
# exponent by squaring

x = 5

print(x)

x = 5**5

print(x)

x = 5**x

print(x)

x = 5**x

print(x)


"""
x = 5

expo = 3125

multiAPart = 1

def chaineExpo(x, expo, multiAPart):
    if expo == 0:
        x = 1
    elif expo == 1:
        x = x
    elif expo % 2 == 0:
        expo = expo / 2
        x = x**2
    elif expo % 2 == 1:
        expo = (expo-1) /2
        multiAPart = multiAPart * x
        x = x**2



while expo > 1:
    chaineExpo(x, expo, multiAPart)
    print(x, "\n E = ", expo, "\n M = ", multiAPart, "\n x = ")

"""


#x = x ** expo
#expo = x
#x = 5






#x**0 = 1
#x ** 1 = x

#x ** (2i) = (x**2) ** i
#x ** (2i) = x * (x**2) ** i

#karatsuba
#xxxx * yyyy = xx*yy truc xx*yy








#x = 5
#print(x)
#print("\n\n")
#x = 5**x
#print(x)
#print("\n\n")
#x = 5**x
#print(x)
#print("\n\n")
#x = 5**x
#print(x)
#print("\n\n")
#x = 5**x
#print(x)
