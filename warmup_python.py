# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
  if talking and hour < 7:
    return True
  elif talking and hour > 20:
    return True
  else:
    return False

 
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)
 


# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# Anot_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str
    
  # str[:3] goes from the start of the string up to but not
  # including index 3