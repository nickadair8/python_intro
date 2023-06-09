import random
from enum import Enum
from lib.dog import bark #import module
import sys
from functools import reduce

#Operating Overloading

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    
roger = Dog("Roger", 3)
syd = Dog("Syd", 4)
print(roger > syd)

#Polymorphism
# class Dog:
#     def eat(self):
#         print("eats dog food")

# class Cat:
#     def eat(self):
#         print("Eating cat food")

# animal1=Dog()
# animal2=Cat()

# animal1.eat()
# animal2.eat()

#list compression
# number = [1,2,3,4]
# numbers_power2 = [n**2 for n in number]
# print(numbers_power2)

#exceptions
# try:
#     result = 2/0
# except ZeroDivisionError:
#     print("can't do that")
# finally:
#     result = 1

# print(result)

#annotation
# def increment(n: int): -> int:
#     return n+1

# count: int=0

""" This is a docstring"""

#recursion
# def factorial(n):
#     if n == 1: return 1
#     return n * factorial(n-1)
# print(factorial(3))

#reduce
# expns = [("Dinner", 20), ("Gas", 30)]
# sum = reduce(lambda a, b: a[1]+b[1], expns)
# print(sum)

#filters
# numbers = [1,2,3,4]
# result = filter(lambda n : n%2 == 0, numbers)
# print(list(result))

#maps
# numbers = [1,2,3,4]
# result = map(lambda a : a * 2, numbers) #calls the functions on the entire list
# print(list(result))

#lambda functions
# lambda num : num * 2
# multiply = lambda a, b : a * b
# print(multiply(2,4))

#accepting arguments\
# name = sys.argv[1]
# print("Hello " + name)

#Modules
# bark()

#classes
# class Animal:
#     def walk(self):
#         print("is walking")

# class Dog(Animal): #inheritance
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print("woof")
    
# roger = Dog("roger", 3)

# print(roger.name, roger.age)
# roger.bark()
# roger.walk()

#loops
# condition = True
# while condition == True:
#     print("cond is true")
#     condition = False
# items = ["Nick", "will", 0, True]
# for item in enumerate(items):
#     print(item)


#functions
# def hello():
#     print("hello")

# hello()

# def talk(phrase):
#     def say(word):
#         print(word)
    
#     words = phrase.split(' ')
#     for word in words:
#         say(word)

# talk("Nick is the best CS kid")

#sets
# set1 = {"Roger", "Syd"}
# set2 = {"Roger"}
# intersect = set1 & set2
# union = set1 | set2
# print(union)
# print(list(set1))

# dictionaries
# dog = {"name": "Roger", "age": 8}
# dog["name"] = "Syd"
# dog["fav food"] = "meat"
# print("name" in dog)
# print(list(dog.items()))


#Tuples
# names = ("Nick", "Will", "Adam")
# sorted(names)
# print(names)

# lists
# dogs = ["Malibu", "Marley", "Mae Mo"]
# humans = ["nick", "will"]
# dogs+=humans
# dogs.remove("will")
# dogs[1:1] = ["Test1", "Test2"]
# print(sorted(dogs,key=str.lower))
# dogsCopy = dogs[:]
# print(dogs)
# print(dogsCopy)

#ENUMS
# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

# print(len(State))


# name = "nick is cool"
# last = ""

# full_name = all([name, last])
# print(full_name)



# def get_choices():
#     player_choice = input("Enter a choice for rock-paper-scissors: ")
#     options = ["rock","paper","scissors"]
#     computer_choice = random.choice(options)
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices

# def check_win(player, computer):
#     print(f"you chose:  {player}  computer chose:   {computer}")
#     if(player == computer):
#         return "It's a tie" 
#     elif(player == "rock" ):
#         if(computer == "scissors"):
#             return "you win"
#         else:
#             return "you lose"
#     elif(player == "paper" ):
#         if(computer == "rock"):
#             return "you win"
#         else:
#             return "you lose"
#     elif(player == "scissors" ):
#         if(computer == "paper"):
#             return "you win"
#         else:
#             return "you lose"

    
# choices = get_choices()
# result = check_win(choices["player"], choices["computer"])
# print(result)


# def greeting():
#     return "Hi"

# choices = get_choices()
# print(choices)

# food = ["pizza", "carrot", "eggs"]
# dinner = random.choice(food)