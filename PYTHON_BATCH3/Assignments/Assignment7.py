numbers = list(map(int, input("Enter the numbers:").split()))
maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
length = len(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
print("Length:", length)


def find_max(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum
def find_min(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum
def find_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total
numbers = list(map(int, input("Enter the numbers: ").split()))
print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
print("Sum:", find_sum(numbers))


def greet(name):
    print("Hello", name + "! Welcome to Python class.")
# Test Case 1
greet("Sairam")
# Test Case 2
greet("Anjali")


def calculate_total(price, quantity):
    total = price * quantity
    return total
# Test Case 1
print(calculate_total(100, 3))
# Test Case 2
print(calculate_total(250, 2))


def create_account(name, role="User"):
    print("Account created for", name, "with role", role)
# Test Case 1
create_account("Rahul")
# Test Case 2
create_account("AdminUser", "Admin")


def square_print(n):
    print(n * n)
def square_return(n):
    return n * n
# Test Case 1
square_print(5)
result = square_return(5)
print(result * 10)
# Test Case 2
square_print(3)


def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
# Test Case 1
print(multiply(add(2, 3), 4))
# Test Case 2
print(multiply(add(10, 5), 2))


def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
# Test Case 1
nums = [1, 2, 3, 4, 5]
even, odd = count_even_odd(nums)
print("Even count:", even)
print("Odd count:", odd)
# Test Case 2
nums = [2, 4, 6]
even, odd = count_even_odd(nums)
print("Even count:", even)
print("Odd count:", odd)


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
# Test Case 1
print(is_palindrome("madam"))
# Test Case 2
print(is_palindrome("python"))



def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n-1)
# Test Case 1
print(factorial(5))
# Test Case 2
print(factorial(4))



n = int(input("Enter n: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


def sum_digits(n):
    if n == 0:          
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
# Test Case 1
print(sum_digits(1234))
# Test Case 2
print(sum_digits(567))


def reverse_string(s):
    if s == "":          
        return s
    else:
        return reverse_string(s[1:]) + s[0]
# Test Case 1
print(reverse_string("python"))
# Test Case 2
print(reverse_string("madam"))


def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
# Test Case 1
countdown(3)
# Test Case 2
countdown(5)


def power(a, b):
    if b == 0:          
        return 1
    else:
        return a * power(a, b-1)
# Test Cases
print(power(2, 3))
print(power(5, 2))
print(power(3, 0))









