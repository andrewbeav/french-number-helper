import random
import sys

# Getting the range
starting_num= input("Number in range to start learning: ")
ending_num = input("Number in range to end with: ")

if (starting_num < 0 or starting_num >= 10000 or ending_num < 0 or ending_num >= 10000):
    print('Range must be greater than 0 and less than 10,000')
    sys.exit()

french_nums = ['zero', 'un', 'deux', 'trois', 'quatre', 'cinque', 'six', 'sept', 'huit', 'neuf',
               'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept',
               'dix-huit', 'dix-neuf']

french_tens = ['dix', 'vingt', 'trante', 'quatrante', 'cinquante', 'soixante', 'soixante-dix', 'quatrante-vingt', 'quatrante-vingt-dix']

while(True):
    num = random.randrange(starting_num, ending_num+1)
    response = input("Say " + str(num) + " in French: ")
    if (num % 10 == num and response == french_nums[num]):
        print('Correct!')
    else:
        break
