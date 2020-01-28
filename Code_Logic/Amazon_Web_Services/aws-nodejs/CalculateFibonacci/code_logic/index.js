function calculateFibonacci(number) {
	if (number === 1 || number === 2) return 1;

	return calculateFibonacci(number - 1) + calculateFibonacci(number - 2);
	
}

var x = 38;

function code() {
	
	return calculateFibonacci(x);

}

module.exports = code
