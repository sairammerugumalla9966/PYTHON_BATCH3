# OOPS --> Object Oriented Programming system


# Paradigms ---> approach / style 

# python supports 3 different paradigms/ approaches 

# procedural approach ---> step by step 
# functional approach ---> use pure functions to solve the problem 
# object oriented approach ---> creating objects to solve the problem 


# What is an Object ??
# object is a byproduct of class 

# properties ----> attributes(variables)
# behaviour ----> functionality (methods / functions)


# what is class ?
# class is a blueprint or design which is used to create objects 

'''
# syntax : 

class ClassName: # creation of class 
    pass 
    # properties(attributes)
    # behaviour (methods)


obj = ClassName()  # object creation / calling 
'''


class Student:
    name = "Naveen"
    id =9966
    course= "python full stack"


obj = Student()
print(obj.name) # sairam
print(obj.id)


obj2 = Student()
obj2.name="keerthi"
print(obj2.name) # keerthi
print(obj2.id)

obj3 = Student()
print(obj3.name) # sairam



# Constructor (__init__) : it is a special method , which automatically executes when an object is created.

class Student1:

    def __init__(self,name, id , course):
        self.name = name 
        self.id=id
        self.course=course


s1 = Student1("keerthi",8975,"pyhton")
print(s1.name)
print(s1.id)
print(s1.course)


s2 = Student1("naveen",8985,"sql")
print(s2.name)
print(s2.id)
print(s2.course)


class BankAccount:

    bankname="Andhra bank" # class variables 
    branchname="l.b.nagar" #class variables 

    def __init__(self, name , balance): # automatically executes 
        self.name=name
        self.balance=balance # instance variable 

    def display(self): # 
        print("your account is created")

    def deposite(self,amount):
        self.balance+=amount

acc1=BankAccount("keerthi",5000)
print(acc1.name)
print(acc1.balance)
print(acc1.bankname)

BankAccount.branchname="secundrabad"
print(acc1.branchname)

acc1.display()
acc1.deposite(2000)
print(acc1.balance)

acc2=BankAccount("naveen",100000)
print(acc2.name)
print(acc2.balance)
print(acc2.bankname)
print(acc2.branchname)









