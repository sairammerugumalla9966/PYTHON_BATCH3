text = "Keerthi"
# uppercase
upper_text = text.upper()
# lowercase
lower_text = text.lower()
print("Uppercase:", upper_text)
print("Lowercase:", lower_text)


text = "Hello World"
text = text.lower()
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Number of vowels:", count)


text = "Hello World"
if text.startswith("Hello"):
    print("String starts with Hello")
else:
    print("String does not start with Hello")


text = "Keerthi Sri"
new_text = text.replace(" ", "-")
print("Updated string:", new_text)


text = "keerthi"
length = text.count("") - 1
print("Length of the string:", length)


text = "madam"
rev = text[::-1]
if text == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


text = input("Enter a sentence: ")
words = text.split()
count = len(words)
print("Number of words:", count)


text = "banana"
ch = "a"
count = text.count(ch)
print("Character appears", count)


text = "  Hello World  "
new_text = text.strip()
print("String after removing spaces:", new_text)


text = "12345"
if text.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")


