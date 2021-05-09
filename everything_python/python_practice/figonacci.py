def fib(end):
    a, b = 0,1
    while a < end:
        print(a, end=' ')
        a,b = b, a+b

fib(189)