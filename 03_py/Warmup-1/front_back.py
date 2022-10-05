#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) == 1:
    return str
  elif len(str) == 2:
    return str[1:] + str[:1]
  else:
    return str[len(str) - 1:] + str[1:len(str) - 1] + str[0:1]
  
print(front_back('code'), "→ 'eodc'")
print(front_back('a'), "→ 'a'")
print(front_back('ab'), "→ 'ba'")
