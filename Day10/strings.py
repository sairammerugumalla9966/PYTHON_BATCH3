# String ??

# sequence of characters
# immutable (will not create new objects)
# order collection 
# indexes and slicing 
# duplicates are allowed 

a="python"
course='python python python full stack'
msg=''' hi ! this is python full stack traing program.
in this we learn everything in practical 
'''

print(msg)
print(course)

print(len(a)) # length of the strings 

name="Sairam"
surname="Merugumalla"

print(name + " " + surname) # concatination

print(name * 3) # repetation is also possible 



# String methods 

name="sai ram"
print(name.lower()) # sairam

print(name.upper()) # SAIRAM

print(len(name))
print(name.strip("@"))

print(name.replace("sai","Sri"))


students="sairam , keerthi , naveen polyshetty ,"
print(students.split(",")) # ['sairam ', ' keerthi ', ' naveen']




# Indexing and slicing 

#Indexing : accessing the individual characters of a string using positions .

surname="Merugumalla"
# +ve index starts from 0 (left to right )
# -ve index starts from -1 (right to left )

print(surname[0])
print(surname[-1])


for char in surname:
    print(char) 



# slicing : extracting subparts of a string 

# string[start : stop : step]

print(surname[0:4]) # step value by default 1

print(surname[4:]) # default stop value "end of the string"

print(surname[: :])

print(surname[: : -1])


# string formatting

print("my name is  ",name)

print("my name is name")

# f strings  , % formatting 


# f- strings

name="keerthi sri devi"
age=24
print(f"my name is {name},my age is {age}")  
 
print(f"{name.capitalize()} is capitalized") # Keerthi sri devi

print(f"{name.title()} ") # Keerthi Sri  Keerthi Sri Devi

salary=50000
bonus=10000
print(f"my total salary = {salary+bonus}")

#salary=int(input("enter salary "))
#bonus=int(input("enter bonus "))
#print(f"my total salary = {salary+bonus}")



# format()

name="keerthi sri devi"
sal=50000
print("my name is {}",format(name))

print("my name is {}".format(name))

print("my name is {} my salary is {}".format(name,sal))


print("my name is %s" % name )














