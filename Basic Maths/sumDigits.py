# sum of digits in a number
def sumOfNum(num):
    sum = 0
    while num>0:
        sum += num%10
        num //= 10
    return sum

# Driver Code
num = int(input("Enter a number: "))
sum_of_digits = sumOfNum(num)
print(f"Sum of digits in {num} is {sum_of_digits}")