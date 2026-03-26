# calculate factorial of a given number
def fact(num):
  fact = 1

  if num==0 or num==1:
    return 1

  for i in range(1, num+1):
    fact *= i

  return fact

#Driver Code
num = int(input("Enter a number: "))
factorial = fact(num)
print(f"Factorial of {num} is {factorial}")