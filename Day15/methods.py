# method ??
# function which is inside a class 

# types :
# Instance method

class Instance_method:

    def intro(self):
        print("executed automatically ")

    def Timepass(self):
        print("timepass successfully done")

obj=Instance_method()
obj.intro()
obj.Timepass()


class Instance_method:

    def __init__(rocky,name):
        rocky.name=name
        print("executed automatically ")

    def Timepass(self): # instance method 
        print(self.name) # instance variable 

obj=Instance_method("Naseem")
obj.Timepass()


# class method

class Class_method:

    name="Meenakshi" # class variable 

    @classmethod  # decorator 
    def Timepass(cls): # class method 
        print(cls.name)


Class_method.Timepass()


# Static method 

class Static_method:

    @staticmethod
    def Timepass():
        name="Meenakshi"
        print(name)

Static_method.Timepass()

# hackerrank -- 2hrs 


