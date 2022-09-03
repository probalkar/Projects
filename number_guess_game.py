import random

number=random.randint(1,100)
guess=int(input("Enter your guess: "))
attempt=1

while(True):
    if guess>number:
        guess=int(input("Too high. Guess again: "))
        attempt+=1
    elif guess<number:
        guess=int(input("Too low. Guess again: "))
        attempt+=1
    else:
        print("Yeah... you guessed right")
        break

print(f"You took {attempt} attempts")