""" Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument """ 
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
  

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len


def main():
  args = sys.argv[1:]
  if check_arguments(args,2):
    print("\n".join(split(args[0],args[1])))
  else:
    print("Error: argument is needed")

main()