let tabOperation = "";

function number(num) {
	tabOperation += num;
}


function operator(operator) {
	tabOperation += operator;
}


function equal() {
	alert(`${tabOperation} = ${eval(tabOperation)}`);
	tabOperation = "";
}

function reset() {
	tabOperation = "";
}

function clean() {
	tabOperation = tabOperation.split("");
	tabOperation.pop();
	tabOperation = tabOperation.join("");
}
