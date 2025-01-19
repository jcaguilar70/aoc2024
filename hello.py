def x2(x):
    return x*2
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a=3
print(x2(a))
print("factorial of",a,"is",fact(a))

print("hello world")
