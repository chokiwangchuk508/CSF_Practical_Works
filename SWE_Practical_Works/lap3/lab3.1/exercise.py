def fibonacci_iterative_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list

# Test the function
print(fibonacci_iterative_list(10))  # Fibonacci numbers up to F(9)
def find_fib_index_exceeding_value(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
print(find_fib_index_exceeding_value(100))  # First Fibonacci number exceeding 100
def is_fibonacci_number(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

# Test the function
print(is_fibonacci_number(21))  # True
print(is_fibonacci_number(22))  # False
def is_fibonacci_number(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

# Test the function
print(is_fibonacci_number(21))  # True
print(is_fibonacci_number(22))  # False
