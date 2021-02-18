

window.addEventListener("load", addListeners);

var console_content = "";

function addListeners() {
    document.getElementById("testButton").addEventListener("click", do_fnct);

}


function do_fnct() {
    alert("test");
    print("hi")
    //document.getElementById("Console").innerHTML = 5 + 6;
}


function addConsole() {
    console_content = document.getElementById("Console").innerHTML;
    console_content = console_content + " Hello";
    document.getElementById("Console").innerHTML = console_content;
}

function myFunction() {
    alert("poop");

}