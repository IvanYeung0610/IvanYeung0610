#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  else:
    return False
  
print(near_hundred(93), "→ True")
print(near_hundred(90), "→ True")
print(near_hundred(89), "→ False")
