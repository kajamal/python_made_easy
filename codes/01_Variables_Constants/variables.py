# Declaring and Assigning variables
speed = 5
Speed = 5.5
average_speed = "5.5kmph"
name = None
print(speed, Speed, average_speed, name)

# Various ways
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# Multi assignment
x,y,z = 1,2.2,"DevOps"
print(x,y,z)

a=b=c=9
print(a,b,c)

x,y,z = 1,2,3
print(x,y,z)

a=b=c=9
print(a,b,c)

# Datatype
speed = 5
Speed = 5.5
average_speed = "5.5kmph"
name = None
print(type(speed), type(Speed), type(average_speed), type(name))

# Objects
name = "DevOps"
print(name.upper())

fruits = ["apple", "orange", "grape"]
fruits.append("banana")
print(fruits)

# Casting
x = 1
print(x, type(x))
x = float(1)
print(x, type(x))

y = int(2.8)
print(y, type(y))

z = str(3.3)
print(z, type(z))

w = float("4.2")
print(w, type(w))

# Memory address
x = 1
print(id(x))  
y = 2
print(id(y))  

x=y=344
print(id(x))  #1621556808976
print(id(y))  #1621556808976


# get id of a variable
a = 12
b = 12
print(id(a))
print(id(b))

# get id of list
a = [1, 2, 3, 4, 5]
print(id(a))

# get id of tuple
a = (1, 2, 3, 4, 5)
print(id(a))
  
# get id of a dictionary
a = {'a' : 1, 'b' : 2}
print(id(a))

# import addressof,
# c_int modules from ctypes module
from ctypes import c_int, addressof

# get memory address of variable
a = 44
print(addressof(c_int(a)))

# get id of a variable in hexadecimal representation
a = 12
print(hex(id(a)))

# get id of list in hexadecimal representation
a = [1, 2, 3, 4, 5]
print(hex(id(a)))

# get id of tuple in hexadecimal representation
a = (1, 2, 3, 4, 5)
print(hex(id(a)))

# get id of a dictionary in hexadecimal representation
a = {'a': 1,'b' : 2}
print(hex(id(a)))

# Data size
import sys
x = 1
print(x ,"occupies", sys.getsizeof(x), "bytes")
x = 2.2
print(x ,"occupies", sys.getsizeof(x), "bytes")
x = True
print(x ,"occupies", sys.getsizeof(x), "bytes")