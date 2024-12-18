#Guido van rossum
import random
num = random.randint(0,100)
flag = False
while not flag:
    a = int(input("Enter the number: "))
    if a > num:
        print("Guess something lesser")
    elif a < num:
        print("Guess something higher")
    else:
        print("You guessed it right")
        flag = True
print("GAME OVER")