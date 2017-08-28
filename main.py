import random
import sys

class num_teacher:
    def __init__(self):
        self.french_nums = ['zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf',
                       'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept',
                       'dix-huit', 'dix-neuf']

        self.french_tens = ['zero', 'dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante',
                            'soixante-dix', 'quatrante-vingt', 'quatrante-vingt-dix']

        self.state = 'GET_RANGE'

    def run(self):

        while(True):
            if self.state == 'GET_RANGE':
                # Getting the range
                self.starting_num= input("Number in range to start learning: ")
                self.ending_num = input("Number in range to end with: ")

                if self.starting_num < 0 or self.starting_num >= 10000 or self.ending_num < 0 or self.ending_num >= 10000:
                    print('Range must be greater than 0 and less than 10,000')
                else:
                    self.state = 'GEN_RANDOM'

            elif self.state == 'GEN_RANDOM':
                self.num = random.randrange(self.starting_num, self.ending_num+1)
                self.state = 'GET_RESPONSE'

            elif self.state == 'GET_RESPONSE':
                self.response = input("Say " + str(self.num) + " in French: ")
                self.state = 'TEST_RESPONSE'

            elif self.state == 'TEST_RESPONSE':
                if self.num < 20 and self.response == self.french_nums[self.num]:
                    self.state = 'CORRECT'
                elif self.num < 100 and self.num % 10 == 0 and self.response == self.french_tens[self.num/10]:
                    self.state = 'CORRECT'
                elif self.num < 71 and self.num % 10 == 1 and self.num < 80 and self.response == self.french_tens[self.num/10]+' et un':
                    self.state = 'CORRECT'
                elif self.num < 70 and self.response == self.french_tens[self.num/10]+'-'+self.french_nums[self.num/10]:
                    self.state = 'CORRECT'
                else:
                    self.state == 'INCORRECT'

            elif self.state == 'CORRECT':
                print('Correct!')
                self.state = 'GEN_RANDOM'

            elif self.state == 'INCORRECT':
                print('Incorrect, try again.')
                self.state = 'GET_RESPONSE'

teacher = num_teacher()
teacher.run()
