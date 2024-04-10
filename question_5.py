# Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def reverse_integer(n):
    negative = n < 0
    
    reversed_str = str(abs(n))[::-1]
    
    reversed_int = int(reversed_str)
    
    if negative:
        reversed_int *= -1
    
    return reversed_int

num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print("Reversed integer:", reversed_num)
