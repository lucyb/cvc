#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

class Cvc(object):

    vowels     = ['a', 'e', 'i', 'o', 'u']
    separator  = '-'

    def __init__(self):
        self.crypto     = random.SystemRandom()
        self.consonants = [letter for letter in string.ascii_lowercase if letter not in Cvc.vowels]
        for i in range(0,3):
            print(self.generate_password())

    def generate_password(self):
        '''Generate a string with random characters in the format cvc-cvc-cvc
        '''
        words = [self.random_word() for i in range(0,3)]
        return Cvc.separator.join(words)

    def random_word(self):
        return self.random_consonant() + self.random_vowel() + self.random_consonant()

    def random_consonant(self):
        return self.crypto.sample(self.consonants, 1)[0]

    def random_vowel(self):
        return self.crypto.sample(Cvc.vowels, 1)[0]
