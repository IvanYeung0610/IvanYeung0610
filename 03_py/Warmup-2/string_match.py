#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  string1 = str(a)
  string2 = str(b)
  counter = 0
  answer = 0
  while counter < len(string1)-1:
    if string1[counter:counter+2] == string2[counter:counter+2]:
      answer+=1
    counter+=1
  return answer
  
print(string_match('xxcaazz', 'xxbaaz'), "→ 3")
print(string_match('abc', 'abc'), "→ 2")
print(string_match('abc', 'axc'), "→ 0")
