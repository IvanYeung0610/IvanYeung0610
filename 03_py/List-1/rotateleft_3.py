#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
  new_nums = nums
  first = nums[0]
  for i in range(len(nums)-1):
    new_nums[i] = nums[i+1]
  new_nums[len(nums)-1] = first
  return new_nums

print(rotate_left3([1, 2, 3]), "→ [2, 3, 1]")
print(rotate_left3([5, 11, 9]), "→ [11, 9, 5]")
print(rotate_left3([7, 0, 0]), "→ [0, 0, 7]")
