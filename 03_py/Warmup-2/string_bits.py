#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  counter = 0
  answer = ""
  while counter < len(str):
    answer += str[counter]
    counter += 2
  return answer
  
print(string_bits('Hello'), "→ 'Hlo'")
print(string_bits('Hi'), "→ 'H'")
print(string_bits('Heeololeo'), "→ 'Hello'")
