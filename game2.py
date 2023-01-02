import random

number = random.randint(1, 20)
attempt=1
guess = int(input("guess the number:"))
while(True):
    if(guess>number):
        guess =int(input("guess another number. this one is too big:"))
        attempt +=1
    elif(guess<number):
        guess =int(input("guess another number. this one is too low:"))
        attempt +=1
    else:
        print(f"your guess is correct.\n no of attempt {attempt}")
        break