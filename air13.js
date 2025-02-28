/* Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre. */

const child_process = require('child_process')
const sys = require('sys')
function run_test(number,argument_string, expected_output,exec_program){
    if (number.toString().length == 1) {
        number = "0" + number;
    }
    let exo_name = ""
    if(exec_program === "python"){
        exo_name = `air${number}.py`
    } else if(exec_program === "node"){
        exo_name = `air${number}.js`
    }

    child_process.exec(`${exec_program} ${exo_name} ${argument_string}`, (error, stdout, stderr) => {
        if(stdout === expected_output){
            console.log(`${exo_name}: \x1b[32msuccess\x1b[0m`)
        } else{
            console.log(`${exo_name}: \x1b[31mfailure\x1b[0m`)
        }
    })
}

function run_python_test(number,argument_string, expected_output){
    run_test(number,argument_string, expected_output,"python")
    
}


function run_node_test(number,argument_string, expected_output){
    run_test(number,argument_string, expected_output,"node")
    
}
function run_tests(){
    run_python_test(0,'"bonjour les gars"',"bonjour\nles\ngars\n")
    run_python_test(1,'"Crevette magique dans la mer des étoilles" "la"',"Crevette magique dans \n mer des étoiles\n")
    run_python_test(2,'"je" "teste" "des" "trucs" " "',"je teste des trucs \n")
    run_python_test(3,'1 2 3 4 5 4 3 2 1',"5\n")
    run_python_test(4,'"Hello milady,   bien ou quoi ??"',"Helo milady, bien ou quoi ?\n")
    run_python_test(5,'1 2 3 4 5 "+2"',"3 4 5 6 7\n")
    run_python_test(6,'Michel Albert Therese Benoit a',"Michel Therese Benoit\n")
    run_python_test(7,'10 20 30 40 50 60 70 90 33',"10 20 30 33 40 50 60 70 90\n")
    run_node_test(8,'10 20 30 fusion 15 25 35','10 15 20 25 30 35\n')
    run_node_test(9,'Michel Albert Therese Benoit','Albert, Therese, Benoit, Michel\n')
    run_node_test(10,'test10.txt','Je danse le mia\n\n')
    run_node_test(11,'O 5','    O    \n   OOO   \n  OOOOO  \n OOOOOOO \nOOOOOOOOO\n')
    run_node_test(12,'6 5 4 3 2 1','1 2 3 4 5 6\n')
}

 run_tests()