#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  if vacation == True or weekday == False:
    return True
  else:
    return False
  
print(sleep_in(False, False), "→ True")
print(sleep_in(True, False), "→ False")
print(sleep_in(False, True), "→ True")
