# Perform the Task
# Perform The Value
# ____________________________________

# def greeting():
#     print("Hello, World!")

# greeting()

# def get_greeting(firstName):
#     return f"Hello, {firstName}!"
# __________________________________________


# USAGE and Benefits of Functions

# def get_greeting(firstName):
#     return f"Hello, {firstName}!"

# greeting = get_greeting("John")

# file=open("greeting.txt", "w")
# file.write(greeting)
# file.close()
# ______________________________________________


# keyword argument

# def increment(number, by):
#     return number + by
# result = increment(2, by=1)
# print(result)  # Output: 3

# __________________________________________________

# optional parameters
# def increment(number, by=1):
#     return number + by
# result = increment(2)

# _____________________________________________________

# *args

# def add_numbers(a, b, c):
#     return a + b + c

# add_numbers(1, 2, 3)

# if we have another numbers how to handle that?
# We can use *args to pass a variable number of arguments.


# _______________________________________________

# def add_numbers(*numbers):
#     print(numbers)
    
# add_numbers(1, 2, 3, 4)  # Output: (1, 2, 3, 4)

#____________________________________________________

# def multiply_numbers(*numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#         return result


# print(multiply_numbers(1, 2, 3, 4))  # Output: 24

# _______________________________________________________

# magic **

# def save_user(**user):
#     print(user)
# save_user(id=1, name="John", age=22, city="New York", mobile="123-456-7890")
# Output: {'id': 1, 'name': 'John', 'age': 22, 'city': 'New York', 'mobile': '123-456-7890'}
# _____________________________________________________________

# SCOPE OF FUNCTIONS

# def greet(name):
#     message='Hello, ' + name

# [OUT OF SCOPE]
# print(name)
# print(message)
# _____________________
# EACH FUNCTION HAS ITS OWN SCOPE

# def greet(name):
#     message='Hello, ' + name
#     print(message)
    
# def email(name):
#     message='Email, ' + name
#     print(message)

#________________________________________________________________

# GLOBAL VARIABLE:[Bad practice]

# message = "temp"

# def greet(name):
    
#     message = 'Hello, ' + name
#     print(message)

# def email(name):
#     global message
#     message = 'Email, ' + name
#     print(message)

# greet("John")
# email("John")

# ________________________________________________________






