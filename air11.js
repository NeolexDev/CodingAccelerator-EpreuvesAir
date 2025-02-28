/* Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre. */

const process = require('process')


function check_arguments(args) {
   if (args.length != 2) {
    console.log("Error: 2 arguments needed")
    return false
   }
   if (args[0].length != 1) {
    console.log("Error: First argument must be a single character")
    return false
   }
   if (Number.isNaN(Number(args[1]))) {
    console.log("Error: Second argument must be a number")
    return false
   }
   return true;
 }
 
 function print_pyramide(char, height){
   for (let i = 0; i < height; i++) {
    console.log(" ".repeat(height-i-1)+char.repeat(i*2 + 1)+" ".repeat(height-i-1))
   }
 }
 
 function main(){
   const args = process.argv.slice(2);
   if (check_arguments(args)) {
      print_pyramide(args[0], args[1])
   }
 }
 
 main()