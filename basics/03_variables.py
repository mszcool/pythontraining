#
# Getting around variables
#

# Declaration
f=0
print(f)

# Re-declaration works in Python (is that really a practice?)
f="abc"
print(f)

# ERROR: combining different types of variables does not work
#print("combining a string with a number does not work " + 123)
print("combining a string with a number does not work " + str(123))

# Global versus Local variables in functions
def foo():
    global f        # tells the function to work on the global f
    f="def"
    print(f)

foo()
print(f)

del(f)
print(f)