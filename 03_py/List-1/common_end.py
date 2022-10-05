#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  if a[0] == b[0]:
    return True
  elif a[len(a) - 1] ==  b[len(b) - 1]:
    return True
  else:
    return False
  
print(common_end([1, 2, 3], [7, 3]), "→ True")
print(common_end([1, 2, 3], [7, 3, 2]), "→ False")
print(common_end([1, 2, 3], [1, 3]), "→ True")
