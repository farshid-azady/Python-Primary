"""
Loop:
    for
    while
"""
for i in range(4):
    print(i , end = ' ')      # 0 1 2 3 

print('\n ==============')    

for i in range(3,8):
    print(i , end= ' ')      # 3 4 5 6 7 
    
    
print('\n ==============')    

for j in range(5,10,2):
    print(j , end = ' ' )   # 5 7 9 

print('\n ==============')    

s = 'farshid'
for ch in s:
    print(ch)
    
print('\n ==============')    

for _ in range(3):
    print('hello')

print('\n ==============')   
 
for i in range(9,2,-3)    :
     print(i , end=' ' )     # 9 6 3 

print('\n ==============')    
     
word = 'python'    
c = 0 
for i in word:
    c+=1
print(c)                # 6

print('\n ==============')    

word = 'alireza'    
c = 0 
for i in word:
    if i =='a':
        c+=1
print(c)                # 2


print('\n ==============')    

name = 'farshid'
v = 'aeiou'
c = 0
for ch in name:
    if ch in  v:
        print(ch)    # a i 
        c += 1
        
print(c)             # 2

print('\n ==============')    

name = 'farshid'
v = 'aeiou'
a = [ch for ch in name if ch in v]
print(a)            # ['a', 'i']

print('\n ==============')    

for i in range(1,4):
    for j in range(2,4):
        print(j,end=' ')
    print()
'''
i = 1  : j=2 , j=3
i = 2  : j=2 , j=3
i = 3  : j=2 , j=3
'''
        
print('\n ==============')    

for i in range(1,4):
    for j in range(2,4):
        print(i,end=' ')
    print()


       
print('\n ==============')    

for i in range(2,5):
    for j in range(i):
        print(j,end=' ')
    print()

'''
i = 2  : j=0 , j=1
i = 3  : j=0 , j=1 , j=2
i = 4  : j=0 , j=1 , j=2 , j=3
'''

print('\n ==============')    
'''
1
1  2
1  2  3
'''

for i in range(2,5):
    for j in range(1,i):
        print(j , end = ' ')
    print()        

    
print('\n # break #')    

for i in range(5):
    if i == 3 :
        break
    else:
        print(i,end=' ')   # 0 1 2 


print('\n # continue #')    

for i in range(5):
    if i == 3 :
        continue
    else:
        print(i,end=' ')   # 0 1 2 4

print('\n ==============')    
for n in range(10,15):
    for i in range(2,n):
        if n % i == 0 :
            print(n , end = ' ')   # 10,12,14
            break
        
print('\n ==============')    
for i in range(3,8):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i , end = ' ')   # 3  5  7
        



print('\n ==============')    

print('# while #')
      
