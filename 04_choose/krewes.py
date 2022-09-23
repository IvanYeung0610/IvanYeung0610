"""
Ivan Yeung
SoftDev
K01 -- Krewes/Python dictionary/We are trying to write a python program that randomly selects a devo from a dictionary
9-22-2022
Time spent: .5

DISCO:
We learned how to import random ("import random as <NAME>")
.choice(<sequence>) method chooses a random element from the sequence

QCC:
Use a new line after the three quotes for the block comment
Can devo be replaced?
Are keys going to be preset or will the keys not be known beforehand?

OPS SUMMARY:
"""

import random as rng
krewes = {2:["devo1","devo2","devo3"], 7:["devo1","devo2","devo3"], 8:["devo1","devo2","devo3"]}
list = [2,7,8]
key = rng.choice(list)
dictionarylist = krewes[key]
print(rng.choice(dictionarylist))
