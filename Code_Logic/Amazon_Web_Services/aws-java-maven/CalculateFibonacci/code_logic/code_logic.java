package code_logic;

public class code_logic {

	static int number = 38;

	public static int calculate_Fibonacci (int x) {
		if (x == 1 || x == 2){
			return 1;
		}
		return (calculate_Fibonacci(x-1) + calculate_Fibonacci(x-2));
	}

	public static int code (){
		return calculate_Fibonacci(number);
	}

}
