#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  for i in nums:
    if i==2 or i==3:
      return True
  return False

print(has23([2, 5]), "→ True")
print(has23([4, 3]), "→ True")
print(has23([4, 5]), "→ False")
