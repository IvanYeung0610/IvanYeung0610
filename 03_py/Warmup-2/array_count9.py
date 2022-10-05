#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  counter = 0
  for i in nums:
    if i == 9:
      counter += 1
  return counter
  
print(array_count9([1, 2, 9]), "→ 1")
print(array_count9([1, 9, 9]), "→ 2")
print(array_count9([1, 9, 9, 3, 9]), "→ 3")
