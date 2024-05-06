def func(x):
    x += 1

def modify_int(x):
    x+=1
    return x

def modify_list(x):
    x.append("WTF")

y = 3 #immutable, for some fucking reason(?), won't be changed by func.
#this apparently comes from everything in python being an object, including integers. They
#are not a primitive type like in C++.
func(y)
print(y)
my_list = ["Geeks", "for"] #is mutable, WILL be changed modify_list
modify_list(my_list)
print(my_list)
y = modify_int(y) #this DOES modify, as expected, though I suspect python is just creating a new int rather than modifying the existing one.
print(y)
print(func) #can print function location
ml = modify_list #can assign variables to function name like an alias
ml(my_list) #and then call it as such?
print(my_list)
y = func(y) #can do this, cause all functions return something even not specified, they return None
print(y)