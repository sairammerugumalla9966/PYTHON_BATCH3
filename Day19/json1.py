# JSON module 
'''
# dumping data into json file

import json

data = {"name": "Sairam", "age": 25}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)


'''
'''
# over writes the data
import json

data = {
    "name": "Sairam",
    "age": 25,
    "course": "Python",
    "company": "ATC",
    "DOB" :"23-03-2026"
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Data written to JSON file")



# reading the Json Data 

import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
print(data["name"])



# loading JSON with List
import json

students = [
    {"name": "Ram", "age": 20},
    {"name": "Sai", "age": 22}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)





import json

name = input("Enter name: ")
age = int(input("Enter age: "))

data = {"name": name, "age": age}

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)

with open("student.json") as f:
    result = json.load(f)

print("Stored Data:", result)

'''