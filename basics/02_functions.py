# 
# Working with functions in python
#

# Simple function
def func1():
    print("I am a function func1")

# Function with arguments
def func2(arg1, arg2):
    print(arg1, " <<and>> ", arg2)

# Function with a return value
def quadrat(x):
    return x * x

# Function with args and defaults
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# Function with multiple arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#
# Running the functions
#

func1()
print(func1())  # func1() does not return anything
print(func1)    # represents the function object

print("calling func2(10,20)")
func2(10, 20)
print("func2(10,20): ", func2(10, 20))
print("quadrat(10): ", quadrat(10))

print("power(10) == ", power(2))
print("power(10, 3) == ", power(2, 3))
print("power(10, 3) == ", power(x = 3, num = 2))

print("multi_add(1,2,3) == ", multi_add(1,2,3))