from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('//Users//macbookairm1//Desktop//SWE_Practical_Works//lap3//lab2//dhsvf.py')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

def count_unique_words(content):
    words = content.lower().split()
    return len(set(words))  # Set removes duplicates

# Test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def find_longest_word(content):
    words = content.split()
    longest_word = max(words, key=len)
    return longest_word

# Test the function
longest_word = find_longest_word(content)
print(f"Longest word: '{longest_word}'")

def count_specific_word(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)

# Test the function
specific_word = "your_word"  # Replace with the word you want to search
specific_word_count = count_specific_word(content, specific_word)
print(f"The word '{specific_word}' appears {specific_word_count} times")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def percentage_longer_than_avg(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

# Test the function
percentage_long_words = percentage_longer_than_avg(content)
print(f"Percentage of words longer than the average: {percentage_long_words:.2f}%")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, count = most_common_word(content)
    longest_word = find_longest_word(content)
    avg_length = average_word_length(content)
    percentage_long_words = percentage_longer_than_avg(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Longest word: '{longest_word}'")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than the average: {percentage_long_words:.2f}%")

# Run the analysis
analyze_text('//Users//macbookairm1//Desktop//SWE_Practical_Works//lap3//lab2//dhsvf.py')
