#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n
    
print(front_times('Chocolate', 2), "→ 'ChoCho'")
print(front_times('Chocolate', 3), "→ 'ChoChoCho'")
print(front_times('Abc', 3), "→ 'AbcAbcAbc'")
