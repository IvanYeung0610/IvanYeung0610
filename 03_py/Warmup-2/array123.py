#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  counter = 0
  while counter < len(nums) - 2:
    if nums[counter] == 1 and nums[counter + 1] == 2 and nums[counter + 2] == 3:
      return True
    counter += 1
  return False

print(array123([1, 1, 2, 3, 1]), "→ True")
print(array123([1, 1, 2, 4, 1]), "→ False")
print(array123([1, 1, 2, 1, 2, 3]), "→ True")
