# Python program to illustrate  
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myfun2(**kkwargs):
    #for arg in argk:
        print("kwargs: ", kkwargs)

myfun2( jeden='Welcome', drugi="chyba", trzeci="taknie" )

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, a+1, sep=' ', end=' ')
        a, b = b, a+b
    print()

fib(4)