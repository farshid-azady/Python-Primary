"""
Python Data Types:
        str , int , float , bool , complex ,list , tuple , set , dict  , bytes , ...
"""

s = "Farshid"  
print(type(s))      # str

i = 2                
print(type(i))      # int

f = 2.5       
print(type(f))      # float


######
c = 2 + 3j          # 2 is the real part and 3 is imaginary
print(type(c))      # complex

######

b = True       
print(type(b))      # bool

print(bool(5))      # True
print(bool(-2))     # True
print(bool('ali'))  # True 

print(bool(0))      # False
print(bool(''))     # False

######

print(bool([]))     # False (empty list)
print(bool({}))     # False (empty dictionary)
print(bool(()))     # False (empty tuple)

###########################

print('--variable names---')
"""
    All identifiers must start with a letter or underscore (_), 
    you can't use digits.
    Identifiers can contain letters, digits and underscores (_). 
    Identifiers can't be a keyword. 
    They can be of any length.
 """

print('a2'.isidentifier())      # True
print('2a'.isidentifier())      # False
print('_myvar'.isidentifier())  # True
print('my_var'.isidentifier())  # True
print('my-var'.isidentifier())  # False
print('my var'.isidentifier())  # False
print('my$'.isidentifier())     # False
print('my#'.isidentifier())     # False

######
# You cannot use reserved words as variable names 

"""
False 	class 	return	is 		finally 
None 	if		for 	lambda 	continue 
True 	def 	from 	while	nonlocal
and 	del 	global 	not 	with
as  	elif 	try		or 		yield
assert 	else 	import 	pass
break 	except 	in 		raise
"""
from keyword import iskeyword
print( iskeyword('if'))   # True

################################

print('---Python Casting---')

i = 5
print(float(i))     # 5.0

######

s ='12'
print(int(s) + 1)   # 13

######

x = 1
c = complex(x)
print(c)            # (1+0j)

########################

n = 12.5
print('%i' % n)     # 12
print('%f' % n)     # 12.500000
print('%e' % n)     # 1.250000e+01

######

a = 5
b = 1
print('Five plus one is {a + b}')    # Five plus one is {a + b}
print(f'Five plus one is {a + b}')   # Five plus one is 6

######

a = b = c = 5       # this statement assign 5 to c, b and a.
print(a, b, c)      # 5 5 5 

######

x = 1         
y = 2         
y, x = x, y         # assign y value to x and x value to y
print(x)            # 2
print(y)            # 1

######

a = 1
b = 2
a, b = b, a + b
print(a)           # 2
print(b)           # 3 

########################
print('---string---')
#Slicing string  Syntax: s[start:end]

s = "Shirafkan"

print(s[0])         # S

print(s[8])         # n

print(s[-1])        # n

print(s[0:4])       # Shir

print(s[:4])        # Shir

print(s[-9:-5])     # Shir

print(s[4:])        # afkan

print(s[4:9])       # afkan

print(s[-5:])       # afkan

########################

l = ["apples", "grapes", "oranges"]  
print(type(l))     # list

######

t = ("apple", "banana", "cherry")	  
print(type(t))     # tuple	

######

d = {'id': '123', 'name': 'farshid'}  
print(type(d))    # dict

######

s = {'apple', 'banana', 'cherry'}    
print(type(s))    # set


########################

#Receiving input from Console 
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = a + b
print(c)