/* Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”. */

const process = require('process');


function get_arrays(args) {
  const index = args.indexOf("fusion")
  const arr1 = args.slice(0,index)
  const arr2 = args.slice(index+1)
  return [arr1,arr2]
}

function sorted_fusion(arr1, arr2){
  let sorted_array = [];
  let i = 0;
  let j = 0;
  while ( i < arr1.length || j < arr2.length ) {
    if (arr1[i] < arr2[j]){
      sorted_array.push(arr1[i])
      i+=1
    }else{
      sorted_array.push(arr2[j])
      j+=1
    }
  }
  return sorted_array
}

function check_arguments(args) {
  if (args.length < 3) {
    console.log("Error: at least 3 arguments are needed");
    return false;
  }
  if (!args.includes("fusion")) {
    console.log("Error: fusion argument is needed");
    return false;
  }
  if (args.filter((arg) => arg === "fusion").length > 1) {
    console.log("Error: fusion argument must be unique");
    return false;
  }   
  const index = args.indexOf("fusion");
  if (index === args.length - 1 || index === 0) {
    console.log("Error: fusion must be in the middle of the arguments");
    return false;
  }
  for (let i = 0; i < args.length; i++) {
    if (isNaN(args[i]) && args[i] !== "fusion") {
      console.log("Error: all arguments must be numbers");
      return false;
    }
  }
  return true;
}

function main(){
  const args = process.argv.slice(2);
  if (check_arguments(args)) {
     let [array1, array2] = get_arrays(args)
     console.log(sorted_fusion(array1,array2).join(" "))
  }
}

main()