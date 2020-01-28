def calculateFibonacci(number):
    if ((number == 1) | (number == 2)): return 1
    
    return calculateFibonacci(number - 1) + calculateFibonacci(number - 2)


def code():
    x = 38
    return calculateFibonacci(x)
