# number of digits in a number
def countDigits(num):
    count = 0
    while num>0:
        count += 1
        num //= 10
    return count

#Driver Code
num = int(input("Enter a number:" ))
count_of_digits = countDigits(num)
print(f"Number of digits in {num} is {count_of_digits}")
