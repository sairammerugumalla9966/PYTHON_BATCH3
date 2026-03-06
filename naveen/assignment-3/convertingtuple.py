my_tuple = (10, 20, 30, 40)
print("original tuple:", my_tuple)
my_list = list(my_tuple)
my_list[2] = 60
my_tuple = tuple(my_list)
print("Modified tuple:", my_tuple)