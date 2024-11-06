import re

def is_dzongkha_word(word):
    return re.match(r'^[\u0F00-\u0FFF]+$', word) is not None

def clean_dictionary(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_words = [word.strip() for word in lines if is_dzongkha_word(word.strip())]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_words))
    print(f"Cleaned dictionary saved to {output_file}")
#files
input_file = '336.txt'
output_file = 'final336.txt'
#Final
clean_dictionary(input_file, output_file)