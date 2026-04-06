def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    return fibonacci(n-1)+ fibonacci(n-2)

# Driver Code
n = int(input("Type the position of the element you want: \n"))
fib_element = fibonacci(n)
print(fib_element)