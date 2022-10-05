#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  answer = ""
  for i in range (len(str)):
    answer += str[:i + 1]
  return answer

print(string_splosion('Code'), "→ 'CCoCodCode'")
print(string_splosion('abc'), "→ 'aababc'")
print(string_splosion('ab'), "→ 'aab'")
