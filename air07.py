""" Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.  """
import sys

def is_number(number):
  return number.replace("-","",1).replace('.','',1).isdigit()

def is_sorted(array):
   for i in range(1,len(array)):
     if array[i] < array[i-1]:
       return False
   return True

def insert_sorted_array(array, insert):
  new_array = [];
  for i in range(len(array)):
    if array[i] < insert:
      new_array.append(array[i])
    else:
      new_array.append(insert)
      break
  for j in range(i,len(array)):
    new_array.append(array[j])
  return new_array

def check_arguments(arguments, required_len):
  return len(arguments) >= required_len

def main():
  args = sys.argv[1:]
  if not check_arguments(args,3):
    print("Error: at least 3 arguments are needed")
    return
  for arg in args:
    if not is_number(arg):
      print("Error: All elements must be numbers")
      return
  arrray = args[:-1]
  if not is_sorted(arrray):
    print("Error: array must be sorted")
    return
  final_array = insert_sorted_array(arrray,args[-1])
  print(" ".join(final_array))

main()