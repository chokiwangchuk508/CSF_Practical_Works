from collections import Counter
import time

def read_file(filename):
    """Read the contents of a file and return it as a string."""
    with open(filename, 'r') as file:
        return file.read()

def count_lines(content):
    """Return the number of lines in the content."""
    return len(content.split('\n'))

def count_words(content):
    """Return the number of words in the content."""
    return len(content.split())

def most_common_word(content):
    """Return the most common word and its count in the content."""
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]  # Returns a tuple (word, count)

def average_word_length(content):
    """Return the average word length in the content."""
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0  # Handle empty content

def analyze_text(filename):
    """Analyze the text in a file and print various statistics."""
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis on your sample file
analyze_text('/Users/macbookairm1/Desktop/SWE_Practical_Works/Lab 2/sample.txt')

# Fibonacci sequence functions
def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """Return the nth Fibonacci number using an iterative approach."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def measure_time(func, n):
    """Measure the execution time of a function."""
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

def fibonacci_generator(limit):
    """Generate the Fibonacci sequence up to the limit."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

def fibonacci_memoized(n, memo={}):
    """Return the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")
