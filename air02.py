""" Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme. """ 
import sys


def join(strings , sep_string):
  ret_str = ""
  for string in strings:
    ret_str += string + sep_string
  return ret_str

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len


def main():
  args = sys.argv[1:]
  if check_arguments(args,2):
    print(join(args[:-1],args[-1]))
  else:
    print("Error: argument is needed")

main()