"""
Ivan Yeung Jeffery Zou
SoftDev
K01 -- Krewes/Python dictionary/We are trying to write a python program that randomly selects a devo from a dictionary
9-22-2022
Time spent: .6

DISCO:
- We learned how to import random ("import random as <NAME>")
- .choice(<sequence>) method chooses a random element from the sequence
- .key() function can be used to look at all the keys in the dictionary that it refers to
- .key() function cannot be used with .choice() as it is and has to be typecasted
- import random as rng renames random so that rng can be used in the functions (e.g. rng.choice()) 

QCC:
- Is devo supposed to be replaced?
- Are the keys for the dictionary defined?
- How does the random method work? How could a function to choose a random number work?
- Will this specific program that we made be used for other programs/projects?

OPS SUMMARY:
(Initial Method)
1. A list of the keys are manually made
2. Used the function rng.choice() to randomly pick key from the list
3. Prints a randomly chosen element from the list that the key referred to
(Second Method)
1. Randomly choose a key using rng.choice() and .keys() functions
2. Prints a randomly chosen element from the list that the key referred to
"""

import random as rng
krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
          7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
          8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]}
"""
list = [2,7,8]
key = rng.choice(list)
dictionarylist = rng.choice(krewes[key])
"""
dictionarylist = rng.choice(list(krewes.keys()))

print("Period: " + str(dictionarylist))
print("Name: " + str(rng.choice(krewes[dictionarylist])))

