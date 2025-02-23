from random import randint

n = randint(1,100)

guesses = 0

a = -1

while (a != n):
    guesses += 1
    a = int(input("Enter the number from 1 to 100: "))
    if (a>n):
        print("Enter a lower number")
    else:
        print("Enter a higher number")

print(f'Congrats! You guessed the correct number in {guesses} and the number is {n}')
