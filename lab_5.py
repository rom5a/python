import re
 
def find_n_character_words(file, n):
    with open(file, 'r') as file:
        content = file.read()
 
    # Use regular expression to find words with 'n' characters
    pattern = r'\b\w{' + str(n) + r'}\b'
    words_with_n_chars = re.findall(pattern, content)
 
    return words_with_n_chars
 
file_name = "file"
n = 3 and 1
result = find_n_character_words(file_name, n)
 
print(f"Words containing {n} characters:")
print(result)
