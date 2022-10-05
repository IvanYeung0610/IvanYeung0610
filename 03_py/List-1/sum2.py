#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
  sum = 0
  if len(nums) < 3:
    for i in nums:
      sum += i
    return sum
  else:
    j = 0
    while j < 2:
      sum+= nums[j]
      j += 1
    return sum

print(sum2([1, 2, 3]), "→ 3")
print(sum2([1, 1]), "→ 2")
print(sum2([1, 1, 1, 1]), "→ 2")
