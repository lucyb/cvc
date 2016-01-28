#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cvc.Cvc import Cvc

def run():
    cvc = Cvc()
    for i in range(0,3):
        print(cvc.generate_password())
