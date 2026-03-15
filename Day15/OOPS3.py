# operator overloading :

# + (addition operator) 5+6
# " im "  +  " fine "

# *args---> multiple arguments    * --> multiplication 

# / ---> division , /n ---> next line  


# polymorphism in function : method overloading 

print("sairam" + "is a don")

print(45 + 67)
# static polymorphism or compile time polymorphism 
# combination of methhod overloading and operator overloading 


# method overridding 
# run time ploymorphism or dynamic polymorphism 

class parent:
    def method1(self):
        print("this is parent method1")
        
    def method(self):
        print("this is parent method")

class child(parent):
    def method1(self):
        print("this is child method")
        print("this is child method")


obj=child()
obj.method1()
# obj.method()


# Abstraction  : hiding implemention details and only show essintial details 

from abc import ABC , abstractmethod

class payment(ABC) : 

    @abstractmethod
    def pay(self , amount):
        pass

class UPI(payment):
    def pay(self , amount):
        print("payment is successful", amount)

obj=UPI()
obj.pay(500)



















