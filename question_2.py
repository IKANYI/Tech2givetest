#Write a program that generates fibonacci sequences up to 100.
def fib(max):
  seq = [0,1]
  while seq[-1] + seq[-2] <= max:
    seq.append(seq[-1] + seq[-2])
  return seq
fib_seq  = fib(100)
print("Fibonacci sequence up to 100:")
print(fib_seq)     
