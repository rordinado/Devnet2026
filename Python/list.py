my_list_var = [1, 2, 3, 4, 5]
print (my_list_var [2])
# list is mutable, meaning you can change its content without changing its identity.. 

# this is to change the list item ar index 4.

my_list_var[4] = 10
print (my_list_var)

# Now lets use tuple. 

# this python proices can serve as range interget if we wanted to view range of interface.
my_tuple_var = ("reyanldo")
print (my_tuple_var [2])
print (my_tuple_var [0:3]) #range


#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

my_dict_var = {"name": "Reynaldo", "age": 30, "city": "New York"}
print(my_dict_var["name"])