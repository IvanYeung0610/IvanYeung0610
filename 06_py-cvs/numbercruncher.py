"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K06 -- numbercruncher/Python dictionary and weighted random/We are trying to write a python program that reads a csv file into a dictionary and randomly choosing one of the keys based on a percentage value
9-29-2022
Time spent: 1.5
DISCO:
- In order to compare quote character, you need to use \" to signify it
- .rfind() method finds the last occurence of an input
- The percentages add up to less than 99.8 calculated in python. Seems to be rounded
QCC:
-Are the quotations supposed to be removed from occupation title?

HOW THIS SCRIPT WORKS:
1. populate_dict reads the entire csv file and splits it based on newlines.
It removes the first element(heading) and the last 2(total percentage and extra newline) from the list.
The function goes through the list of job/percent pairs and puts them into dictionary.
The method used to populate the dictionary with the pairs depends on whether the occupation contains a \" or not.
2. Made a list of occupations from the populated dictionary.
Made a corresponding list of weights from the populated dictionary.
3. choose_weight randomly chooses a number from 0 to 99.8 and continues to aggregate the weights from index 0 until the
sum surpasses the randomly chosen value. When the randomly chosen value is reached, the index of the last added weight
is used to determine the occupation that is choosen.

"""
import random as rng

def populate_dict(dictionary, filename):
    csv_file  = open(filename)
    #.read() parses everything into a string including white space
    # used .split to seperate the occupation/percentage pair
    data = csv_file.read().split("\n")
    #removes the first line since it doesn't count
    total_percentage = data[len(data) - 2]
    data = data[1:len(data) - 2]
    csv_file.close()
    for i in data:
        if i[0] == "\"":
            split_index = i.rfind(",")
            dictionary[i[1:split_index - 1]] = float(i[split_index + 1:])#[1:split_index - 1] removes " at the beginning the end
        else:
            job_weight = i.split(",")
            dictionary[job_weight[0]] = float(job_weight[1])
            
    return total_percentage.split(",")

def choose_weighted(choices, weights): # the choices and weights correspond based on their index in the list
    random_value = rng.random() * 99.8
    #print(random_value)
    value = 0
    index = 0
    while value < random_value:
        value += weights[index]
        index += 1
    return choices[index - 1]


krewes = {} #dictionary holding occupations and percentages
total_percent = populate_dict(krewes, 'occupations.csv')
#print(f'Total Percent: {total_percent}')
#print(krewes)
occupations = list(krewes.keys())
weights = []
#Puts all the percentages into a list
for i in occupations:
    weights.append(krewes[i])
#print(occupations)
#print(weights)

#TESTING WEIGHTED RANDOM
test = {}
for i in occupations:
    test[i] = 0
for i in range(1000):
    test[choose_weighted(occupations, weights)] += 1.0
for i in occupations:
    test[i] /= 10

print(test)
    
    
    
