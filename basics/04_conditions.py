#
# Conditions
#

def main():
    x, y = 100, 100

    if (x < y):
        st = "x is less than y"
    elif(x > y):
        st = "x is greater than y"
    else:
        st = "x is equal to y"

    print(st)
    
    # Conditional statement
    st = "x is less than y" if (x<y) else "x is greater or equal as y"

    print(st)

if __name__ == "__main__":
    main()