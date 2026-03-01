# Datatypes 

# A datatypes means what kind of value a variable is holding and what operations it can perform . 

# numeric datatypes : int , float , complex (numbers)
# intergers : like whole numbers (+ve or 0 or _ve )
# float : decimal numbers 
# complex : 3+4j (imaginary numbers)

# sequence datatype : string , list , tuple, range

# string : all the text (group of characters) ' ' or " " or ''' '''
# supporst indexes 


# list : ordered collection of data 
        # list is declared inside []
        # in this list u can have string , nuumeric 
        # allows duplicates
        # mutable means it can be changed (it will not create new objects) 
        # indexes 

l=[1,2,3,4,5,5,"sairam",99.9]
print(l)
print(type(l))
print(l[0])
print(l[4])
print(l[-1])

# tuple : ordered collection of data 
        # immutable (new objects are created)(can not change)
        #allows duplictes 
        # indexes

t=("sairam", 'keerthi','python', 66,789896,7674.86)
print(t)
print(type(t))

# range :  supports indexes 

# range(start, stop , step)

# default start value : 0
# default stop value : end of the range
# default step value : 1


# boolen data type : True or False 

# Dictionary : stores the values in form of key value pairs 
# ordered 
# mutable
# keys unique 
# {}

d={"trainer":"sairam","trainee":"keerthi","course":"python"}
print(d)

# set : unordered collection  of data 
# {} 
# not duplictes 
# mutable 
# no index 
s={1,1,2,2,3,4,3,4,45,5,6,6}
print(s)

# collection datatypes ?? 
# # list : [] , ordered , mutable, allows duplicates, mixed datatypes , indexes 
# append()
l=[1,2,3,4,5,5,"sairam",99.9]
# # tuple : () ordered , immutable, allows duplicates, mixed datatypes , indexes 
# # set : {} unordered , mutable, no duplicates, mixed datatypes , no indexes
# # dictionary : {"key:value"}  ordered , mutable, allows duplicates,keys unique, mixed datatypes


# nested list  : list inside the list 
l1=[[1,2,3,4],[4,5,6,7],[8,9,0]]
print(l1)

print(l1[0][0])
print(l1[0][1])
print(l1[0][2])


# git clone "http link"
