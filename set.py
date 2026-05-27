# A set is a collection of unique items. 
# It is an unordered collection, which means that the items in a set do not have a specific order. 
# Sets are mutable, which means that you can add and remove items from a set after it has been created.
# no duplicate values
myset = {"apple", "banana", "cherry"} 
print(myset)

myset = {"apple", "banana", "cherry","apple"} 
print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2} # here 1 and True are considered the same value in a set and false and 0 are considered the same value.
print(thisset)



#add set items
thisset2 = {"apple", "banana", "cherry"}
thisset2.add("orange")
thisset2.add("papaya")
thisset2.remove("banana")
print(thisset2)



