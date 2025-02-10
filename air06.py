""" Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères. """
import sys

def contains(string, search):
  for count,char in enumerate(string):
    if char == search[0]:
      tmp_contains = True
      for i in range(1,len(search)):
        if search[i] != string[count+i]:
          tmp_contains = False
      if tmp_contains:
        return True
  return False
      

def delete_element_not_contain(strings, contain_string):
  ret_array = []
  for string in strings:
    if not contains(string.lower(),contain_string.lower()):
      ret_array.append(string)
  return ret_array


def check_arguments(arguments, required_len):
  return len(arguments) >= required_len


def main():
  args = sys.argv[1:]
  if not check_arguments(args,2):
    print("Error: at least 2 arguments are needed")
    return
  final_array = delete_element_not_contain(args[:-1],args[-1])
  print(" ".join(final_array))

main()