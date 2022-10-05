#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  evens = 0
  for i in nums:
    if i % 2 == 0:
      evens += 1
  return evens

print(count_evens([2, 1, 2, 3, 4]), "→ 3")
print(count_evens([2, 2, 0]), "→ 3")
print(count_evens([1, 3, 5]), "→ 0")

