def first_non_repeating_char():
  string = "himachal"
  str_lst = [l for l in string]
  r=0
  for l in str_lst:
    for i in range(len(string)):
      index = string[i:i+1]
      if l == index:
        r += 1
    if r > 1:
      r = 0
    else:
      print(l + " " "first not repeating character")
      break
    
  return l

print(first_non_repeating_char())

#without using a list
def first_non_repeating_char():
  string = "jayanto"
  
  r=0
  for l in string:
    for i in range(len(string)):
      index = string[i:i+1]
      if l == index:
        r += 1
    if r > 1:
      r = 0
    else:
      print(l + " " "is the first not repeating character")
      break
    
  return l

print(first_non_repeating_char())
