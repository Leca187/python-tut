# print("lecaop")

# ------------------------------------------------------------------------
# VARIABLE = kontener za variable

# first_name = "leca"
# last_name = "levent"
# full_name = first_name + " " + last_name
# print(type(first_name))
# print(full_name)
# print("Zdravo" + " " + first_name + " " + last_name)

# age = 25
# age += 1
# print(age)
# print(type(age))
# print("Imas"+ " " + str(age) + " " + "godina")

# height = 175.05
# print(height)
# print(type(height))
# print("Tvoja visina je "+" "+ str(height)+"cm")

# human = False 
# print(human)
# print(type(human))
# print("Are you a human:" +" "+ str(human))
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# MULTIPLE ASSIGMENT = dodeljivanje vise vrednosti u istoj liniji

# name, age, attractive = "leca", 25, True

# leca, djora, buaa, saki = 30
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# STRING metode u pythonu

# name = "leca leven"

# print(len(name))
# print(name.find("n"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("e"))
# print(name.replace("e","W"))
# print(name*3)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Type casting = vrednost iz jednog tipa u drugi

# x = 1
# y = 2.0
# z = "3"

# x = float(x)
# y = str(y)
# z = int(z)

# print(x)
# print(y)
# print(z)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# INPUT

# name = input("What is your name: ")
# age = int(input("How old are you: "))
# age = age + 1
# height = float(input("How tall are you: "))
# print("Hello "+name)
# print("You are " + str(age) + " years old")
# print("You are "+ str(height) + "cm " + "tall")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# MATH

# import math

# pi = 3.14
# x = 1
# y = 2
# z = 3 

# print(round(pi))
# print(math.ceil(pi)) #zaokruzi gornja
# print(math.floor(pi)) #zaokruzi donja
# print(abs(pi)) #apsolutna vrednost
# print(pow(pi,2)) #kvadrat
# print(math.sqrt(9))
# print(max(pi,x,y,z))
# print(min(pi,x,y,z))
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#Slicing String

            # indexing[] or slice()
            # [start:stop:step]

# name = "Leca Leven"

# first_name = name[0:4:1] #[:4]
# last_name = name[5:10:1] #[4:]
# funky_name = name[0:10:2] #[::2]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://facebook.com"
# slice = slice(7,-4)

# print(website1[slice])
# print(website2[slice])
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# if statement = deo koda koji ce se izvrsiti ako je if uslov ispunjen

# age = int(input("How old are you: "))

# if age == 100:
#     print("You are century old!")
# elif age >= 18:
#     print("You are an adolt!")
# elif age < 0:
#     print("you haven't been born yet")
# else:   
#     print("You are a child!")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Logical operators (or,and,not) dva ili vise stejtventa isntinita ili ne

# temp = int(input("what is the temperature outsisde: "))

# if temp >= 0 and temp < 30:
#     print("the temerature is ok today")
# elif temp<0 or temp >30:
#     print("temp is bad today")

# if not(temp >= 0 and temp < 30):
#     print("temp is bad today")
# elif not(temp<0 or temp >30):
#     print("the temerature is ok today")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# WHILE loop - deo koda koji ce se izvrsavati sve dok je argumet tacan

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")
# print("hello " + name)

# name = None

# while not name:
#     name = input("Enter your name: ")
# print("hello " + name)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# FOR loop izvrsava deo koda odredjeni broj puta

# import time

# for i in range(10):
#     print(i+1)

# for i in range(50,100,2):
#     print(i)

# for i in "leca leven":
#     print(i)

# for secondes in range(10,0,-1):
#     print(secondes)
#     time.sleep(1)
# print("hello")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# NESTED LOOP - unutrasnji loop ce se ceo izvrsiti pre sledceg koraka spoljasnjeg loopa

# rows = int(input("how many rows?: "))
# columns = int(input("how many columns?: "))
# symbol = input("enter the symbol?: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol + " ", end="")
#     print()
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Loop Control Statements

# break =      izlazak iz loopa
# continue =   preskace do sledece interacije loopa
# pass =       ne radi nista

# while True:
#     name= input("enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,20):
#     if i == 13:
#         pass
#     else:
#         print(str(i) + " ", end="")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#  lIST - koristi se za cuvanje vise stvari u istoj varijabli

#food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
# print(food[0])

# food[0] = "sushi"

# food.append("ice cram")
# food.remove("hotdog")
# food.pop()
# food.insert(1, "cake")
# food.sort()
# food.clear()

# for i in food:
#     print(i)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#2D LISTS - lista u listi

# drinks = ["coffee", "soda", "tea"]
# dinner= ["pizza","hamburger","hotdogs"]
# dessert = ["cake","ice cream"]

# food = [drinks, dinner, dessert]

# print(food[0][0])
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# TUPLE - kolekcija koja je ordered o nepromenjiva
#         sluzi grupisanju slicnih podataka

# student = ("leca",25,"male")

# print(student.count("leca"))
# print(student.index("male"))

# for i in student:
#     print(i)
# if "leca" in student:
#     print("leca is here!")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# SET - kolekcija koja nije po redu, neindexsirana i bez duplikata
#       brze od liste
# utensils = {"fork","spoon","knife"}
# dishes = {"bowl", "plate", "cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# for i in utensils:
#     print(i)

# dinner_table = utensils.union(dishes)
# for i in dinner_table:
#     print(i)

# print(utensils.difference(dishes))    #sta ima utensils a dishes nema
# print(utensils.intersection(dishes))  #sta imaju zajednicko
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# DICTIONARY - promenjiva, ne po redu kolekcija jedinstvenih key:value parova
#              brze jer koristi hashing, dozvoljava da se brzo pristupi vrednosti

# capitals = {
#     "USA": "Washington DC",
#     "India": "New Delhi",
#     "china": "Beijing",
#     "Russia": "Moscow"
# }

# capitals.update({"Germanu": "Berlin"})
# capitals.update({"USA": "New York"})
# capitals.pop("China")
# capitals.clear()

# print(capitals["Russia"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# INDEX OPERATOR [] - omogucava pristup elementu sekvence (str,list,tuples)

# name = "leca Leve!"

# if name[0].islower():
#     name = name.capitalize()
# print(name)

# first_name = name[0:4].upper()
# last_name = name[5:].lower()
# last_caracter = name[-1]

# print(first_name)
# print(last_name)
# print(last_caracter)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# functions - blok koda koji se izvrsava samo kada je pozvan

# def hello(name,lastname, age):
#     print("hello! " + name)
#     print("have a nice day! " + lastname)
#     print("you are "+ str(age) + " years old")

# my_name = "leca"
# last_name = "Doca"

# hello(my_name,last_name,21)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# RETURN STATEMENT - funkcije salju python vrednosti/objekte nazad ko ih poziva
#                    ove vrednosti/objekti su poznati kao povratne vrednosti funkcija

# def multiply(number1,number2):
#     resault = number1 * number2
#     return resault

# x = multiply(5,4)

# print(x)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# KEYWORD ARGUMENTS - 

# def hello(first,middle,last):
#     print("Hello "+first +" "+middle+" "+last)

# hello(last="Leve", middle="Dejan", first="Leca")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# NESTED FUNCTION CALLS - pozivanje funkcija unutar funkcija
#                         unutrasnje funkcije se pozivaju prve
#                         return vrednosti se koriste za sledecu iznad

# num=input("Unesi ceo pozitivni broj: ")
# num=float(num)
# num=abs(num)
# num=round(num)
# print(num)

# print(round(abs(float(input("Unesi ceo pozitivan broj: ")))))
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# SCOPE - Region u kome je varijabla vidljiva
#         varijabla je dostupna samo u regionu u kome je kreirana
#

# name = "Leca"           # Global socpe (dostupna unutar i izvan funkcija)

# def display_name():
#     name = "Leve"       # Local scope (dostupna samo u funkciji)
#     print(name)

# display_name()
# print(name)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# *args - parametar koji ce spakovati sve argumente u tuple
#         korisno zato sto funkcija moze da prihvati varirajuci broj argumenata

# def add(*numbers):
#     sum = 0 
#     numbers = list(numbers)
#     numbers[0] = 0
#     for i in numbers:
#         sum += i
#     return sum
    
# print(add(1,2,3,4,5,6))
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# **kwargs - parametar koji ce spakovati sve argumente dikseneri

# def hello(**imena):
#     # print("hello "+ nesto["first"] + " " + nesto["last"] )
#     print("hello", end=" ")
#     for i,j in imena.items():
#         print(j, end=" ")

# hello(tittle="Mr.", first="Leca", middle="dejan", last="Leve")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# str.format() - opciona metoda koja daje vecu kontrolu prilikom prikazivanja outputa

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over "+item)
# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(item,animal)) #positional argument
# print("The {animal} jumped over the {item}".format(item="moon",animal="cow")) #keyword argument

# text = "The {} jumped over the {}"

# print(text.format(animal,item))

# name = "Leca"

# print("hello my name is {}".format(name))
# print("hello my name is {:10}".format(name)) #dodavanje paddinga
# print("hello my name is {:<10}".format(name)) #dodavanje paddinga desno
# print("hello my name is {:>10}".format(name)) #dodavanje paddinga levo
# print("hello my name is {:^10}".format(name)) #dodavanje paddinga centar

# number = 1000

# print("The number pi is {:.2f}".format(number)) #f za float i broj za broj decimala
# print("The number is {:,}".format(number))      #zarez za hiljaditi deo
# print("The number is {:b}".format(number))      #binarni prikaz
# print("The number is {:o}".format(number))      #oktalni prikaz
# print("The number is {:X}".format(number))      #heksadekadni prikaz
# print("The number is {:E}".format(number))      #"naucni" prikaz
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# random modul

# import random

# x = random.randint(1,6)     #random broj izmenju 1 i 6 
# y= random.random()          #random broj izmenju 0 i 1 sa zarezom

# mylist = ["rock", "paper", "scissors"]
# z= random.choice(mylist)

# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)

# print(x,y,z,cards)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# exception - 
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator/denominator
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("you cant devide by 0")
# except ValueError as e:
#     print(e)
#     print("enter only numbers")
# except Exception as e:
#     print(e)
#     print("something went wrong")
# else:
#     print(result)
# finally:
#     print("this will always execute")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# File detection

# import os

# path = "C:\\Users\\aleks\\Desktop\\Python\\test.txt"
# path2 = "C:\\Users\\aleks\\Desktop\\Python\\test"

# if os.path.exists(path2):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else: 
#     print("That location doenst exists!")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Read file in python
# try:                                    #try i exept ako file ne postoji da izbaci gresku
#     with open("test.txt") as file:      #with open automatski zatvara file
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")

# print(file.closed)                      #da li je file zatvoren
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Writing files in python

# text = "What is this maaaan\nThis is some text\nHave a good one!"

# with open("test.txt","a") as file:  # "a" za append, "w" za write, "r" za read
#     file.write(text)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# copy files in python

# copyfile() - kopira sadrzaj filea
# copy()     -  copyfile() + permission mode + destination can be directory
# copy2()    - copy() + copies metadata (file's creation and modificition times)

# import shutil

# shutil.copyfile("test.txt","test\\copy.txt") #sorce, destination
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# moving files or directory

# import os

# source = "test2.txt"
# destination = "test\\test2.txt"

# try:
#     if not os.path.exists(source):
#         print("This file dont exist")
#     elif os.path.exists(destination):
#         print("there is alredy a file there")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# delete files using python

# import os
# import shutil

# path = "test\\test3.txt"
# path1 = "empty_folder"

# try:
#     # os.remove(path)           # ne brise prazne foldere
#     #os.rmdir(path1)            # ne brise foldere koji sadrze files
#     shutil.rmtree(path1)        # brise folder i sve u njemu

# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You dont have promition to delete that")
# except OSError:
#     print("You can not delete that using that function")
# else: 
#     print(path1+" was deleted")
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------













