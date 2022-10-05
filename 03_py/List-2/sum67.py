#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
  total = 0
  ind = 0
  while ind < len(nums):
    if nums[ind] == 6:
      while nums[ind] != 7:
        ind += 1
    else:
      total += nums[ind]
    ind += 1
  return total

print(sum67([1, 2, 2]), "→ 5")
print(sum67([1, 2, 2, 6, 99, 99, 7]), "→ 5")
print(sum67([1, 1, 6, 7, 2]), "→ 4")
