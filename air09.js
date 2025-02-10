/* Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation. */

const process = require('process');

function ma_rotation(array) {
   let new_array = []
   for(let i = 1; i < array.length; i ++){
      new_array.push(array[i])
   }
   new_array.push(array[0])
   return new_array
}

function check_arguments(args) {
  if (args.length < 2) {
   console.log("Error: At least 2 arguments needed")
   return false
  }
   return true;
}


function main(){
  const args = process.argv.slice(2);
  if (check_arguments(args)) {
     console.log(ma_rotation(args).join(", "))
  }
}

main()