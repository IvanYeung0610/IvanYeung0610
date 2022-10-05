#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  new_nums = nums
  larger = 0
  if(nums[0] >= nums[len(nums)-1]):
    larger = nums[0]
  else:
    larger = nums[len(nums)-1]
  for i in range(len(nums)):
    new_nums[i] = larger
  return new_nums

print(max_end3([1, 2, 3]), "→ [3, 3, 3]")
print(max_end3([11, 5, 9]), "→ [11, 11, 11]")
print(max_end3([2, 11, 3]), "→ [3, 3, 3]")
