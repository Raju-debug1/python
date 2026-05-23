#stores data in key-value pairs
#mutable(can be changed)
#keys must be unique
#values can be of any data type
student = {
    "name": "John Doe",
    "age": 20,
    "class": "12"
}
print(student["name"])  #john doe
print(student["age"])   #20
student["school"] = "ABC High School"  #Adding new key
student["age"] = 223                    #Update value
print(student)

del student["class"]

print(student)

print(student.keys())   #All keys
print(student.values()) #All values
print(student.items())  #pairs


