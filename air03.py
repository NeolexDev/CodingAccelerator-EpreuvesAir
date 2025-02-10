""" Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire. """

import sys

def ret_intruder(strings):
  count_map = {}
  for string in strings:
    if string not in count_map:
      count_map[string] = 1
    else:
      count_map[string] += 1
  return [k for k, v in count_map.items() if v == 1][0]

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len

def main():
  args = sys.argv[1:]
  if check_arguments(args,2):
    print(ret_intruder(args))
  else:
    print("Error: at least 2 argument is needed")

main()

