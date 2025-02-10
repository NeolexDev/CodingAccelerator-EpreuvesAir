/* Créez un programme qui affiche le contenu d’un fichier donné en argument. */
const fs = require('node:fs');
const process = require('process')

function return_file_content(filename){
   try{
      fs.accessSync(filename, fs.constants.R_OK)
      return data = fs.readFileSync(filename, 'utf8');
   }catch(error){
      return error.message
   } 
}

function check_arguments(args) {
   if (args.length < 1) {
    console.log("Error: At least 1 arguments needed")
    return false
   }
    return true;
 }
 
 
 function main(){
   const args = process.argv.slice(2);
   if (check_arguments(args)) {
      console.log(return_file_content(args[0]))
   }
 }
 
 main()