numbers = [45, 2, 67, 55, 98, 100]
largest = smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)