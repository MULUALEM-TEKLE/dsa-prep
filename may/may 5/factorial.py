# with a loop
def factorial_loop(n):
    result = 1
    while n >= 1 :
        result *= n
        n -= 1

    return result

# print(factorial_loop(5))


# with recursion

def factorial_recursion(n):
    if n == 1: 
        return 1 

    return n * factorial_recursion(n-1)

print(factorial_recursion(5))