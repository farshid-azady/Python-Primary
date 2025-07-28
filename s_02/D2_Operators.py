"""
find codes at : 'https://github.com/farshid-azady/Python-Primary'
Operators :
    Arithmetic : +,-,*,/,%,**,//   
    Assignment : =,+=,-=,*= ,/= ,%= ,//= ,**= 
    Comparison : ==,!=,>,<,>=,<=
    Logical    : and, or, not
    Membership : in , not in
    Bitwise    :  &, |, ^, ~, <<, >>
"""

print('Arithmetic Operators')

#Addition
print(1 + 3)       # 4

#Subtraction
print(5 - 3)       # 2

#Multiplication
print(2 * 3)       # 6

#Float Division
print(3 / 2)       # 1.5
 
#Integer Division
print(3 // 2)      # 1

#Remainder
print(17 % 5)      # 2

# Exponentiation
print(2 ** 3)      # 8 
print(0 ** 0)      # 1
print(6 ** 0)      # 1

####################################################

print('Operator Precedence')

print(8 - 2 * 3)                    # 2
print(1 + 3 * 4 / 2)                # 7.0
print(16 / 2 ** 3)                  # 2.0
print(2**2**3)                      # 256

####################################################

print('Augmented Assignment Operator')

x = 4
x += 2    # x = x + 2
print(x)  # 6

y = 8
y //= 2   # y = y // 2
print(y)  # 4

####################################################

print('Comparison Operators')

print(2 == 3)                       # False
print(2 != 3)                       # True
print(2 < 3)                        # True

print('Logical Operators') 

print(1<3  or 4>5)                  # True
print(1<3 and 4>5)                  # False
print(not 1<3)                      # False

# 'Short-circuit'
print(1 >= 2 and (5/0) > 2)         # False

#print(3 >= 2 and (5/0) > 2)        # division by zero

####################################################

print('Membership Operators')

x = [1,2,3,4,5]
print(3 in x)                       # True
print(24 not in x)                  # True

####################################################

print('Bitwise Operators')

a = 13
print(bin(a))                       # 1101

b = 14
print(bin(b))                       # 1110

###

c = a | b
print(bin(c))                      # 1111

###

c = a & b
print(bin(c))                      # 1100

###

c= a ^ b
print(bin(c))                      # 0011 

###

a = 13
print(a << 1)                      # 26

###

a = 20
print(a >> 1)                     # 10

###

a = 18
print(a >> 2)                     # 4

####################################################

print('--- Operations on string ---')

s1 = 'Farshid'
s2 = ' azadi'
s3 = s1 + s2
print(s3)                        # Farshid Shirafkan

###

s = 'sara'
print(2*s)                       # sarasara

####################################################

#Every object in python is stored somewhere in memory. 
#We can use id() to get that memory address.

s1 = 'farshid'
s2 = 'farshid'
print(id(s1)==id(s2))            # True

s1 += ' azadi'

print(id(s1)==id(s2))            # False

###############################################
print()

print(abs(-4))             # 4
print(pow(2,3))            # 8
print(divmod(8,4))         # (2,0)
print(round(2.6))          # 3
print(abs.__doc__)         # 'Return the absolute value of the argument.'

print('# math #')

import math
print( math.sqrt(4))       #2.0
print( math.trunc(2.3))    #2
print( math.floor(2.3))    #2
print( math.ceil(2.3))     #3
print( math.factorial(4))  #24
print( math.log2(32))      #5.0
print( math.log10(100))    #2.0
print( math.e)             #2.7
print( math.log(32))       #3.46
print( math.sin(5))        #-0.9
print( math.fmod(9,4))     #1.0
print( math.gcd(30,4))     #2
print( math.fabs(-4))      #4.0
print( abs(-4))            #4
print( math.pow(2,3))      #8.0
print( pow(2,3))           #8
print( math.pi)            # 3.141592653589793
print(f'{math.pi :.2f}')   # 3.14

print('# random #')
import random
print( random.randint(1, 5))  
print( random.choice([1,5]))  
a = [1,2,3,4]
random.shuffle(a)
print(a)

print('# datetime #')

import datetime
now = datetime.datetime.now()
print(now)                     # 2020-05-16
print( now.year)               # 2020
print( now.month)              # 2020
print( now.day)                # 16

print('# sys , platform ,os #')
import sys
print( sys.version)           # 3.7.3
print( sys.platform)          # win32

import platform
platform.release()            # 10

import os 
print(os.getcwd())            #'C:\\Users\\Farshid-pc2'
