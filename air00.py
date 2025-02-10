""" Créez un programme qui découpe une chaîne de caractères en tableau """ 
import sys
from tabnanny import check


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

def check_arguments(arguments):
  return len(arguments)


def main():
  args = sys.argv[1:]
  if check_arguments(args):
    print("\n".join(split(args[0]," \t\r\n")))
  else:
    print("Error: argument is needed")

main()