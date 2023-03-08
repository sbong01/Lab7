#Lab 7
#author: saerin bong and katherine O'Roark

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
        return value


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
