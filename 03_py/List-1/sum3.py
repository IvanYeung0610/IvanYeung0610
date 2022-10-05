#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

print(sum3([1, 2, 3]), "→ 6")
print(sum3([5, 11, 2]), "→ 18")
print(sum3([7, 0, 0]), "→ 7")
