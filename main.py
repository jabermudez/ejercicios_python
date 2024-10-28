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