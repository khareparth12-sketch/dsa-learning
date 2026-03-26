# Palindrome Number Check
def palNum(num):
  rev, temp = 0, num
  while temp>0:
    rev = (rev*10) + (temp%10)
    temp //= 10

  if rev==num:
     return True
  else:
    return False

# Driver Code
num = int(input("Enter a number: "))
palNumber = palNum(num)
if palNumber:
  print(f"The number {num} is a palindromic number.")
else:
  print(f"{num} is not a palindromic number.")