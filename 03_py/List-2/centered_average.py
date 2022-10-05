#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
  ans = 0
  high = nums[0]
  low = nums[0]
  for n in nums:
    ans += n
    high = max(n, high)
    low = min(n, low)
  return (ans - high - low)/(len(nums)-2)

print(centered_average([1, 2, 3, 4, 100]), "→ 3")
print(centered_average([1, 1, 5, 5, 10, 8, 7]), "→ 5")
print(centered_average([-10, -4, -2, -4, -2, 0]), "→ -3")
