#
# Working with Classes in Python
#

class MyTestClass():
    
    def fooOne(self):
        print("This is function MyTestClass.fooOne()")

    def fooTwo(self, someArgument):
        print("This is function MyTestClass.fooTwo() --> ", someArgument)

    def fooThree(self, someArgument):
        print("This is function MyTestClass.fooThree()")
        self.fooOne()
        self.fooTwo(someArgument + " from fooThree()!")

class MyTestClassTwo(MyTestClass):
    def __initialize__(self, test1, test2):
        print(test1)
        print(test2)
    
    def fooOne(self):
        print("I am the derived class' fooOne()!!")

    def fooOneFromTwo(self):
        print("I am an extension of base fooOne")
        self.fooOne()
    
    def fooTwo(self):
        MyTestClass.fooTwo(self, "from the derived")
        print("I am another derived method, but I called the base class method")

def main():
    print("Welcome to classes!")

    c = MyTestClass()
    c.fooOne()
    c.fooTwo("Hey There!")
    c.fooThree("Hey There 2!")

    c2 = MyTestClassTwo()
    c2.fooOne()
    c2.fooOneFromTwo()
    c2.fooTwo()

if __name__ == "__main__":
    main()