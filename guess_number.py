from random import randint
random_number = randint(0,9)
print random_number

guess = 11
while random_number != guess:
	guess = int(raw_input("Guess a number from 0 to 10! \n"))