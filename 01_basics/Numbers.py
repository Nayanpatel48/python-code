x=2
y=3
z=4
print(x+y)

# precision is important
print((x+y)*z)
print(x+(y*z))

# print('nayan'+3)
# both value datatype should be same

print(int(20.90))
# 20

print('chai'+'code')

print(x+1, y+2)
# 3 5

print(y%2)
# 1

print(z**7)
# 16384

print(100**2)
print(x**100)

result = 1/3.0
print(result)

print(repr('chat'))

print(str('chat'))

print('chat')

print(1<2)
print(1==1)
print(1 != 2)

print(x<y<z)

print(x<y and y<z)
print(1<2 or 1<0)

print(1==2<3)

print(1 == 2 and 2 < 3)

import math

# closest value below number
print(math.floor(3.5))
print(math.floor(-3.5))

print(math.trunc(2.8))
print(math.trunc(-2.8))

print(99999999999999999+1)

print(999999999999*2.9)

print((2+1j)*3)

# octal numbers
print(0o20)
# 16

print(0xFF)

print(0b1000)

print(oct(64))
# 0o100

print(bin(64))

print(int('64', 16))
# 100

# Bitwise operator
x=1
print(x<<2)

print(x | 2)

import random
print(random.random())

l1=['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))
# gives you random values

# shuffle
print(l1)
random.shuffle(l1)
print(l1)

print(0.1 +0.1+0.4)
print(0.1+0.1+0.1)

# print(0.1+0.1+0.1 -0.3)
# problematic

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))
# 0.3

from fractions import Fraction
myFra = Fraction(2, 7)
print(myFra)

# set dataset
setone = {1,2,3,4}
#intersection
print(setone & {1,3})
# Union
print(setone | {1,3,5,7})

print(setone-{1,2,3,5,4})

print(type({}))
# dictionary