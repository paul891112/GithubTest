# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:07:06 2022

@author: paul8
"""

import random

def generate():
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    while (a==b or a==c or a==d or b==c or b==d or c==d):
        b = random.randint(0,9)
        c = random.randint(0,9)
        d = random.randint(0,9)
    ret = str(a) + str(b)+str(c)+str(d)
    return ret
    
    
def takeguess(solution):
    guess = input("Enter your guess: ")
    while len(guess)!=4:
        guess = input("Invalid format, please reenter your guess: ")
    if guess == solution:
        return False
    A=0
    B=0
    Z="A: "
    for i in range(0,4): #index for guess
        for j in range(0,4): #index for solution
            if guess[i] == solution[j]:
                if i==j:
                    A += 1
                    Z += str(guess[i])
                else:
                    B += 1
    print(str(A) + "A" + str(B) + "B")
    print(Z)
    return True
            


print("Welcome to game")
solution = generate()
print("A random number has been generated, please enter 4 numbers")
playing = True
playing = takeguess(solution)
count=1
while playing:
    playing=takeguess(solution)
    count += 1
print("Solution: "+solution)
if count>5:
    print("Sorry, you used more than 5 guesses, you lost")
else:
    print("Congrats, you won! It only took " + str(count) + " rounds!")












