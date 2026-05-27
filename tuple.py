# to convert list into tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

# to convert tuple into list
my_tuple = (1, 2, 3, 4, 5) 
my_list = list(my_tuple)
print(my_list)  


my_string = "Hello, World!"
my_tuple = tuple(my_string)
print(my_tuple)

my_string = "Hello, World!"
my_list = list(my_string)
print(my_list)

# to convert tuple into string
my_tuple = ('H', 'e', 'l', 'l', 'o')
my_string = ''.join(my_tuple)
print(my_string)

# to convert dict into tuple
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_tuple = tuple(my_dict.items())
print(my_tuple)


# to convert tuple into dict
my_tuple = (("name", "Alice"), ("age", 30), ("city", "New York"))
my_dict = dict(my_tuple)
print(my_dict)


# to convert dict into list
my_dict = {"name": "Alice", "age": "30", "city": "New York"}
my_list = list(my_dict.items())
print(my_list)
