/*
    A function declaration consists of the function keyword, followed by the name of the 
    function, then a list of parameters to the function enclosed in parentheses and separated 
    by commas.

    The function body is enclosed in curly brackets, {} and holds all code to be run
    when the function is called.

    To call a function, simply type the function name and pass the appropriate arguments.
*/

// Writing a function declaration
function sayHello(){
    console.log("Hello World!");
    console.log("Have a great day!");
}

// Calling a function
sayHello();
sayHello();
sayHello();

// Writing a function declaration with paramaters.
function sayHi(name, mood){
    alert("Hello " + name);
    alert("I understand you are " + mood);
}

// Calling the function
let userName = prompt("What is your name: ");
let userMood = prompt("What is your mood: ");
sayHi(userName, userMood);

// Writing a function with a return value.  
function addFive(number){
    alert("Adding 5 and " + number);
    return number + 5;
    alert("This will not run because we've used a return and the function stops!");
}

// Calling funciton and getting the return value.
let myNumber = parseInt(prompt("Enter a number: ")); //parseInt() or parseFloat()
console.log(typeof(myNumber));
let sum = addFive(myNumber);
alert(sum);

