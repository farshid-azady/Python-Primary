'''
Control statements:
    if
    if else
    elif
'''
import math
n = -16
# n = int(input('enter:'))
if n < 0 :
   n = abs(n)
   
print(math.sqrt(n))                # 4

print('=====================')

a = 5
if True:
    a = 6
print(a)                           # 6

print('=====================')

a = 20
if a % 2 == 0:
    print('evevn')                  # even
else:    
    print('odd')

print('=====================')

x = 3
y = 2
if x == 1 or y == 1:   # if 1 in(x,y)
    print('ok')
else:
    print('no')                      # no
 
print('=====================')

names = ['sara','taha','farshid']
if 'ali' in names:
    print('found')
else:
    print('not found')               # not found
    
print('=====================')
print('conditional expression')

a = 2
b = 5

#if a < b:
#    m = a
#else:
#    m = b

m = a if a < b else b    

print(m)    

print('=====================')

my_list  = ['a','e','o','i','u']

#if 'o' in my_list:
#    s = 'yes'
#else:
#    s = 'no'

s = 'yes' if ('o' in my_list) else 'no'  # yes
print(s)    

print('=====================')

x = 2
y = 6

z = 1 + ( x if x > y else y+2)

print(z)                                 # 9

print('=====================')

grade = 12
s = 'fail' if grade < 10 else 'pass'
print(s)                                # pass

print('=====================')

today = 'holiday'
b = 25000

if today == 'holiday':
   if b > 20000:
       print('shopping')              # shopping
   else:
       print('watch TV')
else:
    print('normal working day')

print('=====================')

score = 75

if score >= 90:
    l = 'A'
else:
  if score >= 80 :
      l = 'B'
  else:
       if score>= 70:
           l = 'C'
       else :
           l = 'D'

print(l)                          # C     

print('elif')  
     
score = 75

if score >= 90:
    l = 'A'
elif score >= 80 :
    l = 'B'
elif score>= 70:
    l = 'C'
else :
    l = 'D'
    
print(l)                          # C     

print('=====================')

x = -2
y = -4

if x > 0 and y > 0 :
    print('A')
elif x > 0 and y < 0 :
    print('B')    
elif y > 0:
    print('C')                   # D
else:
   print('D')    
   

print('=====================')

age = 47
gender ='M'

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
                                     


print('=====================')

w = 75        # w = float(input('weight in kilo:'))
h = 1.74      # h = float(input('height in meter:'))

bmi = w / (h ** 2)

if bmi < 15:
    c = 'very severely underweight'
elif 15 <= bmi <= 16 :
    c = 'severely underweight'
elif 16 < bmi <= 18.5:
    c = 'underweight'
elif 18.5 < bmi <= 25:
    c = 'Normal'
elif 25 < bmi <= 30:
    c = 'overweight'
elif 30 < bmi <= 35:
    c = 'moderately obese'
elif 35 < bmi <= 40:
    c = 'severely obese'
elif bmi > 40:
    c = 'very severely obese'

print('Your BMI = ' + str(bmi) + ' You are ' + c + '.')
