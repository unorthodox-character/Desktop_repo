''' good practice of returning a function'''
def fib(arg):
    result = []
    a,b = 0,1
    while a < arg:
        result.append(a)
        a,b = b,a+b
    return result

print(fib(378), end=' ')