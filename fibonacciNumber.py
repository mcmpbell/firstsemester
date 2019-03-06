def fibonacciNumber(n):

    if n == 1:
        return(1)
    if n == 0:
        return(0)

    else:
        fibonacci = [0, 1]
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        fibonacci_string = ", ".join(str(a) for a in fibonacci)
        print(fibonacci_string)

x = int(input("What is your number? "))

fibonacciNumber(x)
