def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

fib_string = ""
for i in range(20) : 
    fib_string += f"{fib(i)} => "

print(fib_string)

