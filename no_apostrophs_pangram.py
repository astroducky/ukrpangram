#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:48:14 2018

@author: maks
"""

#This checks, whether imput is an ukrainian pangram

inputphrase='Жебракують скотиняки при ґанку церкви в Гадячі, ще й шатро їхнє знаємо.'
inputphrase=inputphrase.lower()

ukralphabet=set()
ukralphabet.update(['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
             'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'])


lettersinphrase=set()
for letter in inputphrase:
    if letter in ukralphabet:
        lettersinphrase.add(letter)

if lettersinphrase==ukralphabet:
    print('This is a pangram')
    print('Length of input =', len(inputphrase))
else:
    print('This is not a pangram')
    print('There is no following letters:', ukralphabet.difference(lettersinphrase))

