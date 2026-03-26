# print all Prime numbers in an Interval
def is_prime(num):
  for i in range(2, num):
    if num%i == 0:
      return False
  return True

# Driver code
a, b = map(int, input("Enter start and end of range: ").split())

for i in range(a, b+1):
  if is_prime(i):
    print(i)