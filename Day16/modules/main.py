# modules  ---> user-defined , in-built modules 
# packages
# virtual enviroonment (important) 



# modules ---> .py extention , it is a python file containing functions , classes , variables , code.

# uses 

# reuse code 
# for better maintaince 
# 


import calculator

print(calculator.add(10,5))
print(calculator.sub(10,5))

print(calculator.name)



import math as m

print(m.sqrt(81))

print(m.pi)



from math import sqrt , pi # from module_name import function/class 

print(m.sqrt(81))
print(m.pi)


from Day16.modules import calculator

from modules.calculator import add


