'''
name = input("Cual es tu nombre?: ")
age= int(input("Cuántos años tienes? "))

age += 2

print(f'El señor {name}, tiene {age} años')
'''

#INDEX : 
# slicing = create a substring by extracting elements from another string
#           index[] or slice()
#           [start:stop:step]
'''xnombre = "Alexander bermudez"

primer_nombre = nombre[:3]
apellidos = nombre[4:]
nombre_raro = nombre[0:17:2]
nombre_reverso = nombre[::-1]

print(nombre_reverso)

'''
'''
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
'''

#if statement = a block of code that will execute if it's condition is tru
'''
age = int(input("Cuantos años tienes?: "))

if age == 100:
    print("Tu eres un anciano")
elif age >18:
    print("Eres un adulto")
elif age < 0:
    print("No has nacido")
else: 
    print("tu eres menor de edad")

'''

#logical operators (and, or, not) = used to check if two or more conditional statements are true
'''
temp = int(input("Cual es la temperatura afuera?: "))

if temp >= 0 and temp <= 30:
    print("La temperatura esta bien afuera")
    print("Puede salir")
elif temp < 0 or temp > 30:
    print("La temperatura no está bien")
    print("Quedate adentro")

'''

#while loop = a statement tha will execute it's block of code,
#               as long as it's condition remains true
'''
name = None

while not name:
    name = input("Ingrese su nombre: ")

print("Hola "+name)
'''

#for loop =  a statement that will execute it's block of code
#             a limited amout of times
#   
#             while loop = unlimited
#             for loop = limited
'''
for i in range(10):
    print(i+1)

for i in range(50,100+1):
    print(i)

for i in range(80,100+1,5):
    print(i)



for i in "alexander bermudez":
    print(i)


import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Feliz Navidad!")
'''

#nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
'''
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

'''

#Loop Control Statements = change a loops execution fron its normal sequence

# break = use to terminate the loop entirely
# continue = skips to the next iteration of the loop.
# pass = does nothing, acts as a placeholder

'''
while True:
    name = input("Ingrese su nombre: ")
    if name != "":
        break


phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")



for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
    
'''

#list = use to store multiple items in a single variable

#food = ["pizza","hamburguesa","perros","carnitas"]
#food[0] = "sushi"

#print(food[0])
#food.append("Ice Cream")
#food.remove("perros")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()


#for x in food:
#    print(x)

# 2D list = a list of lists
'''
drinks = ["coffee","soda","tea"]
dinner = ["pizza", "hamburguesa", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks,dinner,dessert]

print(food[2][1])
'''

#tuple = colletion which is ordered and unchangeable
#        used to group together related data

'''
student = ("Alex", 21, "masculino")

print(student.count("Alex"))
print(student.index("masculino"))

for x in student:
    print(x)

if "Alex" in student:
    print("Alex está aquí")
'''

#set = collection which is unordered, unindexed. No duplicate values
'''
utensilios = {"fork", "spoon","knife"}
platos = {"bowl","plate","cup","knife"}


#utensilios.add("napkin")
#utensilios.remove("fork")
#utensilios.clear()
#utensilios.update(platos)
#tabla_comida = utensilios.union(platos)

#print(utensilios.difference(platos))

print(utensilios.intersection(platos))
#for x in tabla_comida:
 #   print(x)

 '''

#dictionary = A changeable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly
'''
capitals = {'USA':'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Rusia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()

#print(capitals['India'])
#print(capitals['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key,value)

'''

#index operator [] = gives access to a sequence's element (str, list, tuples)
'''
name = "alexander bermudez!"

#if (name[0].islower()):
 #   name = name.capitalize()

first_name = name[0:3].upper()
last_name = name[10:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

'''

#Function = a block of code which is executed only when it is called.
'''
def hello(first_name, last_name, age):
    print("Hola "+first_name+" "+last_name)
    print("Tu tienes "+str(age)+" años")
    print("Que tengas un bonito día")

hello("Alex", "Bermudez", 48)

# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value

def multiply(number1, number2):
    return number1 * number2

x = multiply(6,5)

print(x)
'''

# key arguments = arguments preceded by an identifier when we pass them to a function
#                 The order of the arguments doesn't matter, unlike positional arguments
#                 Python knows the names of the arguments that our function receives
'''
def hello(first, middle,last):
    print("hello "+first+" "+middle+" "+last)

hello(last="Bro",middle="Dude",first="Code")
'''
#nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

#num = input("Ingrese un numero positivo: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("Ingrese un numero positivo")))))

#scope = The region that a variable is reorganized
#        A variable is only available fron inside the region it is created.
#        A global and locally scoped versions of a variable can be created.
'''
name = "Bro" # global scope (available inside & outside functions)

def display_name():
    name = "Code"  # Local scope (availabe only inside this function)
    print(name)

display_name()
print(name)
'''

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
'''def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
'''

# **kwargs = parameter that will pack all arguments into a dictionaty
#            useful so that a function can accept a varying amount of keyword argument
'''

def hello(**kwargs):
    #print("Hello " + kwargs['first'] +  " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Bro", middle="Dude", last="Code")
'''

# str.format() = optional method that gives users
#                more control when displaying output
'''

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {1}".format(animal,item)) # positional argument
print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Alex"

print(("Hello, my name is {}".format(name)))
print(("Hello, my name is {:10}. Nice to meet you".format(name)))
print(("Hello, my name is {:<10}. Nice to meet you".format(name)))
print(("Hello, my name is {:>10}. Nice to meet you".format(name)))
print(("Hello, my name is {:^10}. Nice to meet you".format(name)))

number = 3.14159

print("The number pi is {:.2f}".format(number))

number1 = 1000

print("The number is {:.3f}".format(number1))
print("The number is {:,}".format(number1))
print("The number is {:b}".format(number1))
print("The number is {:o}".format(number1))
print("The number is {:X}".format(number1))
print("The number is {:E}".format(number1))
'''

#Random
'''
import random

x = random.randint(1,6)
y = random.random()

myList = ['rock','paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)

'''
#exception = events detected during execution that interrupt the flow of a program
'''
try: 
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide bye: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divede by zero! Idiot")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")

'''

import os 

path = "C:\\Users\\SENA\\OneDrive\\Escritorio\\file"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else: 
    print("That location doesn't exist?")