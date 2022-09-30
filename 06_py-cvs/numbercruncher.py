"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K06 -- numbercruncher/Python dictionary and weighted random/We are trying to write a python program that reads a csv file into a dictionary and randomly choosing one of the keys based on a percentage value
9-29-2022
Time spent: .5
DISCO:
- In order to compare quote character, you need to use \" to signify it
- .rfind() method finds the last occurence of an input
QCC:
-Are the quotations supposed to be removed from occupation title?

HOW THIS SCRIPT WORKS:

"""
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
            
    return total_percentage


krewes = {} #dictionary holding occupations and percentages
total_percent = populate_dict(krewes, 'occupations.csv')
print(f'Total Percent: {total_percent}')
print(krewes)
