students = ["keerthi","lally","sravani","prasad","pawan"]
print("Original List:", students)
students.append("Mahesh")
print("After Adding one more name:", students)
students.remove("keerthi")
print("Final List:", students)



numbers = [22,18,9,14,2,16]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
  if num > largest:
     largest = num
  if num < smallest:
     smallest = num
print("List:",numbers)
print("Largest Element:", largest)
print("Smallest Element:", smallest)



my_tuple = ("Keerthi", 22, 85.5, True, "Python")
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])     
print("Second element:", my_tuple[1])    
print("Third element:", my_tuple[2])     
print("Fourth element:", my_tuple[3])    
print("Last element:", my_tuple[-1]) 
print("\nTuples are immutable because they do not support methods")
print("like append(), remove(), or item assignment.")
print("Once created, their elements cannot be changed.")



numbers = [10, 20, 30, 20, 40, 10, 50, 30]
print("Original List:", numbers)
unique_numbers = list(set(numbers))
print("List After Removing Duplicates:", unique_numbers)



employee = {
    "id": 101,
    "name": "Keerthi",
    "salary": 25000
}
print("Original Dictionary:", employee)
employee["department"] = "IT"
print("\nAfter Adding New Key:", employee)
employee["salary"] = 30000
print("\nAfter Updating Salary:", employee)
del employee["id"]
print("\nAfter Deleting a Key:", employee)



student = {
    "id": 22,
    "name": "Keerthi",
    "course": "Python",
    "marks": 90
}
print("Keys:")
for key in student.keys():
    print(key)
print("\nValues:")
for value in student.values():
    print(value)
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)



set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Set 1:", set1)
print("Set 2:", set2)
union_set = set1.union(set2)
print("Union:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)



numbers = [10, 20, 30, 20, 10, 40, 30, 10]
print("Original List:", numbers)
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("\nFrequency of each element:")
for key, value in frequency.items():
    print(key, ":", value)

    

List:
A list is an ordered and changeable (mutable) collection. It allows duplicate values.
Syntax: []
Example:
shopping_list = ["Milk", "Bread", "Eggs", "Milk"]
print(shopping_list)

Tuple:
A tuple is ordered but unchangeable (immutable). It allows duplicates.
Syntax: ()
Example:
numbers = (10,20,30,10)
print(numbers[2])

Set:
A set is unordered and does not allow duplicate values.
Syntax: {}
Example:
student_ids = {101, 102, 103, 101}
print(student_ids)

Dictionary:
A dictionary stores data in key-value pairs.
Syntax: {key: value}
Example:
employee = {
    "id": 22,
    "name": "Keerthi",
    "salary": 30000
}
print(employee)


