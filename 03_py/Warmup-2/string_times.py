#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  return str * n

print(string_times('Hi', 2), "→ 'HiHi'")
print(string_times('Hi', 3), "→ 'HiHiHi'")
print(string_times('Hi', 1), "→ 'Hi'")
