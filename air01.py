import sys

def count_split(line , sep_string):
  count = 1
  for c in line:
    for c2 in sep_string:
      if c == c2:
        count += 1
        break
  return count

def split(line , sep_string):
  array = ["" for i in range(count_split(line , sep_string))]
  index = 0
  last_is_sep = False

  for c in line:
    found = False
    for c2 in sep_string:
      if c == c2:
        if not last_is_sep:
          index += 1
          last_is_sep = True
          continue
    if not last_is_sep:
      array[index] += c
    last_is_sep = False
  return array  
  
if len(sys.argv) < 2:
  print("usage: " + sys.argv[0] + " string")
  sys.exit(1)
print(split(sys.argv[1] , " \t\n"))