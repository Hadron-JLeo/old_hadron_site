
/*
window.addEventListener("load", addListeners);
function addListeners() {
    document.getElementById("testButton").addEventListener("click", addConsole());
}
*/

/* Event onLoaded */
window.addEventListener("load", start_bot);


var console_content = "";

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

function console_print(input) {
    write_in_console(input);
}

function write_in_console(input) {
    console_content = document.getElementById("Console").innerHTML;
    console_content = console_content + String(input) + " ";
    document.getElementById("Console").innerHTML = console_content;
    //return console_content;
}

async function start_bot() {
    my_text = "Starting bot";
    write_in_console(my_text);
    await sleep(1000);
    calculate_gas();
}

function calculate_gas() {
    var gas = 4;
    write_in_console(gas + 5);
}

