function calculateFibonacci(number) {
	if (number === 1 || number === 2) return 1;

	return calculateFibonacci(number - 1) + calculateFibonacci(number - 2);
	
}

function code() {
	var x = 38;
	return calculateFibonacci(x);
}

module.exports = code
