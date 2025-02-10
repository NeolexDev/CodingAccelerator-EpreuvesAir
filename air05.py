""" Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste."""
import sys

def is_number(number):
  return number.replace("-","",1).replace('.','',1).isdigit()

def check_array_is_number(numbers):
  for num in numbers:
    if not is_number(num):
      return False
  return True

def parse_operation(operation):
  number = int(operation[1:])
  if operation[0] == "-":
    return -number
  else:
    return number  

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len


def do_operation(numbers,operation):
  operation_value = parse_operation(operation)
  ret_numbers = []
  for num in numbers:
    ret_numbers.append(int(num)+operation_value)
  return ret_numbers


def main():
  args = sys.argv[1:]
  if not check_arguments(args,2):
    print("Error: at least 2 arguments are needed")
    return
  if not check_array_is_number(args[:-1]):
    print("Error: firsts arguments must be numbers")
    return

  result_numbers = do_operation(args[:-1],args[-1])
  print(" ".join([str(num) for num in result_numbers])) 

def check_arguments_len(arguments, required_len):
  return len(arguments) >= required_len

main()

