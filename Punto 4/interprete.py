import time

def factorial_python(n):
    if n == 0:
        return 1
    else:
        return n * factorial_python(n-1)


start_time = time.time()
result = factorial_python(35)
end_time = time.time()

print(f"Python Factorial of 35: {result}")
print(f"Python Execution Time: {end_time - start_time} seconds")