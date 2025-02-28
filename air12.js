/* Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort). */

const process = require('process')

function array_to_number(array){
   let ret_array = []
   array.forEach(numberString => {
      ret_array.push(Number(numberString))
   });
   return ret_array
}

function check_arguments(args) {
   if (args.length < 2) {
    console.log("Error: At least 2 arguments needed")
    return false;
   }
   for(const element of args){
      if(Number.isNaN(Number(element))){
         console.log("Error: All argument must be numbers")
         return false;
      }
   }
   return true;
 }

 function quicksort(numbers){
   if (numbers.length <= 1){
      return numbers
   }
   let array_left = []
   let array_right = []
   let array = [...numbers]
   let pivot = numbers[numbers.length-1]
   array.pop()
   
   array.forEach((number) => {
      if (number < pivot){
         array_left.push(number)
      } else {
         array_right.push(number)
      }
   })
   return quicksort(array_left).concat(pivot).concat(quicksort(array_right));
 }

 
 function main(){
   const args = process.argv.slice(2);
   if (check_arguments(args)) {
      array = array_to_number(args)
   }
   console.log(quicksort(array).join(" "))
 }
 
 main()