#!/usr/bin/env python

import random
import string

class Cvc(object):

    vowels     = ['a', 'e', 'i', 'o', 'u']
    consonants = [letter for letter in string.asscii_lowercase if not in vowels]
    separator  = '-'

    def __init__(self):
        self.crypto = random.SystemRandom()
        for i in range(1,3):
            password = self.generate_password()
            print(password)

    def generate_password(self):
        '''Generate a string with random characters in the format cvc-cvc-cvc
        '''
        words = [self.random_word() for i in range(1,3)]
        return separator.join([words])

    def random_word(self):
        return self.random_consonant() + self.random_vowel() + self.random_consonant()

    def random_consonant(self):
        return crypto.sample(consonants, 1)

    def random_vowel(self):
        return crypto.sample(vowels, 1)
