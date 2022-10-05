#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  substring = str[len(str) - 2 :]
  answer = 0
  counter = 0
  while counter < len(str) - 2:
    if substring == str[counter: counter + 2]:
      answer += 1
    counter += 1
  return answer
  
print(last2('hixxhi'), "→ 1")
print(last2('xaxxaxaxx'), "→ 1")
print(last2('axxxaaxx'), "→ 2")
