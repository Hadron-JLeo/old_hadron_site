
/*
window.addEventListener("load", addListeners);


function addListeners() {
    document.getElementById("testButton").addEventListener("click", addConsole);

}

*/

var console_content = "";


function addConsole() {
    console_content = document.getElementById("Console").innerHTML;
    console_content = console_content + " Hello";
    document.getElementById("Console").innerHTML = console_content;
}

function myFunction() {
    alert("poop");

}
