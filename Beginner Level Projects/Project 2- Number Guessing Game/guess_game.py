#importing random module so that we can select numbers randomly
import random

print("Welcome to guess game !")

random_nbr = random.randrange(0,11)
'''randrange is used to select number from the starting range till ending range (excluding end).'''

print ("Guess my number! (hint : between 0 and 10)")
user_nbr = int (input ("Enter your guess: "))


while user_nbr != random_nbr : #Our loop will run untill the user guess it correct.
    if (user_nbr > random_nbr):
        print("My number is below from your guess !")
    else:
        print("My number is above from your guess !")
    user_nbr = int (input ("Enter your guess: "))
else:
    print("Congrats! you guessed it right my number is ",random_nbr)
    

