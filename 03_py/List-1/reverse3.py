#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  new_nums = nums
  first = nums[0]
  for i in range(len(nums)):
    new_nums[i] = nums[len(nums)-1-i]
  new_nums[len(nums)-1] = first
  return nums

print(reverse3([1, 2, 3]), "→ [3, 2, 1]")
print(reverse3([5, 11, 9]), "→ [9, 11, 5]")
print(reverse3([7, 0, 0]), "→ [0, 0, 7]")
