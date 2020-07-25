#
# Loops (for, while and co)
#

def main():
    x = 0

    print("while...")
    while( x < 5 ):
        print(x)
        x = x + 1

    print("for (is an interator)...")
    for x in range(5, 10):
        print(x)

    print("use a for loop over a collection")
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    print("break in a loop")
    for x in range(5, 10):
        if(x == 7): break
        print(x)   

    print("continue in a loop")
    for x in range(5, 10):
        if(x == 7): continue
        print(x)   

    print("using enumerate() function to get indices")
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i, d)

if __name__ == "__main__":
    main()