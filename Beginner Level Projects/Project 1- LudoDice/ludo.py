#importing random module so that we can select numbers randomly
import random

print("Welcome to ludo game !")

random_nbr = random.randint(1,6)
'''randint is used to select number from the starting range till ending range
you can also use random_nbr = random.randrange(1,7) to get the above thing here we write 7
because the randrange exclusive the ending number'''

print("Hey! you have got a",random_nbr,"number dice.")

