#Write a program that takes an integer as input and returns true if the input is a power of two.
def power_of_two(n):
  return n > 0 and (n & (n - 1)) == 0
n = int(input("Enter an integer: "))
result = power_of_two(n)
print(f"{n} is a power of two: {result}")
