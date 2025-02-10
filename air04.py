""" Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents."""
import sys

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len

def remove_adjacent(string):
  ret_string = ""
  last_char = ""
  for i in range(len(string)):
    current_char = string[i]
    if current_char != last_char:
      ret_string+=current_char
    last_char = current_char
  return ret_string

def main():
  args = sys.argv[1:]
  if check_arguments(args,1):
    print(remove_adjacent(args[0]))
  else:
    print("Error: at least 2 argument is needed")

main()

