#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  if hour<7 or hour>20:
    if talking == True:
      return True
  return False

print(parrot_trouble(True, 6), "→ True")
print(parrot_trouble(True, 7), "→ False")
print(parrot_trouble(False, 6), "→ False")
