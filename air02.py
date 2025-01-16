import sys

def count_split(line , sep_string):
  count = 0
  total = 1
  for c in line:
    if c == sep_string[count]:
      count += 1
    else:
      count = 0
    if count == len(sep_string):
      total+=1
      count=0

  return total

def split(line , sep_string):
  array = ["" for i in range(count_split(line , sep_string))]
  index = 0
  count = 0
  for c in line:
    if c == sep_string[count]:
      count+=1
    else:
      count = 0
    if count == 0:
      array[index] += c
    if len(sep_string) == count:
      count = 0
      index+=1
  return array  
  
if len(sys.argv) < 2:
  print("usage: " + sys.argv[0] + "string separator")
  sys.exit(1)
print("\n".join(split(sys.argv[1] , sys.argv[2])))