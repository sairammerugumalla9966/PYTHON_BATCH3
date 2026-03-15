'''
# Encapsulation : binding data(variables) and methods together inside a class 
# and restrict direct access to some objects 


# access specifiers 

# public ---> variable 
# private ---> __variable
# protected ---> _variable 



class BankAccount:

    def __init__(self, balance): # automatically executes 
        self.__balance=balance # instance variable 

    
    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
 
acc=BankAccount(5000)
acc.deposite(2000)
acc.withdraw(1000)
print(acc.get_balance())


# Inheritance : allows child class to inherit the attributes and methods of parent class 
# child class and parent class 

# why ??
# code reuse 
# duplicate code reduces 
# creating relationships 

class employee: # parent class 
    def show(self):
        print("employee working ")

class manager(employee):  # child class
    def manage(self):
        print("manages the team")


obj = manager()
obj.show()
obj.manage()

obj1=employee()
obj1.show()


# types of inheritance

# single inheritance 

class employee: # parent class 
    def show(self):
        print("employee working ")

class manager(employee):  # child class
    def manage(self):
        print("manages the team")


obj = manager()
obj.show()
obj.manage()

obj1=employee()
obj1.show()


# multiple inheritance  (more than one parent classes )


class employee1: # parent class 
    def show(self):
        print("employee1 working ")


class employee2: # parent class 
    def display(self):
        print("employee2 working ")


class manager(employee1,employee2):  # child class
    def manage(self):
        print("manages the team")


obj = manager()
obj.show()
obj.display()
obj.manage()

obj1=employee2()
obj1.show()
obj1.display()

# multi level inheritance 
class grandparent: # grandparent class 
    def show(self):
        print("can use grandparent(their own) properties")


class parent(grandparent): # parent class 
    def display(self):
        print("can use parent and grandparent properties")


class child(parent):  # child class
    def manage(self):
        print("can use child , parent and grandparent properties")


# hierarichical inheritance 

class parent: # parent class 
    def show(self):
        print("can use grandparent(their own) properties")


class child1(parent): # child class 
    def display(self):
        print("can use parent and grandparent properties")


class chidl2(parent):  # child class
    def manage(self):
        print("can use child , parent and grandparent properties")

# hybrid inheritance 
'''

# polymorphism : poly ---> many  morphs ---> forms 

# same method or function behaves differently denpending on the object 

# +  ----> addition operator 
# + ---> concatination operator ??

print("python" + "programming")

print(10+29)


#* --->multiplication 
#*args --->variable length args 

print(11 * 3)
print("hi" * 3)








