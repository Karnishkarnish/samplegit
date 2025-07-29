s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
string'''
text = "Python"
print(text[0])    # 'P'
print(text[-1])   # 'n'
text = "HelloWorld"
print(text[0:5])    # 'Hello'
print(text[5:])     # 'World'
print(text[::-1])
s1 = "apple"
s2 = "banana"
print(s1 == s2)       # False
print(s1 < s2)  
print(len("hello"))

s = "Python3"

print(s.isalpha())   # False (has digit)
print(s.isdigit())   # False
print("123".isdigit())  # True
print("abc".isalpha())  # True

text = "  Hello World! Welcome to Python Programming.  "

# 1. lower(): Converts to lowercase
print(text.lower())  
# Output: "  hello world! welcome to python programming.  "

# 2. upper(): Converts to uppercase
print(text.upper())  
# Output: "  HELLO WORLD! WELCOME TO PYTHON PROGRAMMING.  "

# 3. strip(): Removes leading and trailing spaces
print(text.strip())  
# Output: "Hello World! Welcome to Python Programming."

# 4. replace(): Replaces a substring
print(text.replace("Python", "Java"))  
# Output: "  Hello World! Welcome to Java Programming.  "

# 5. split(): Splits the string into a list
words = text.strip().split(" ")  
print(words)  
# Output: ['Hello', 'World!', 'Welcome', 'to', 'Python', 'Programming.']

# 6. join(): Joins a list into a string with a separator
joined = "-".join(words)
print(joined)  
# Output: "Hello-World!-Welcome-to-Python-Programming."

# 7. startswith(): Checks if string starts with given value
print(text.strip().startswith("Hello"))  
# Output: True

# 8. endswith(): Checks if string ends with given value
print(text.strip().endswith("Programming."))  
# Output: True

# 9. find(): Returns first index of substring
print(text.find("World"))  
# Output: 8

# 10. count(): Counts how many times a substring appears
print(text.count("o"))  
# Output: 5
