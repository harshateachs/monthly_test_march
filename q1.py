def print_pattern1(n):
    for i in range(1, n + 1):
        print('* ' * i)

def print_pattern2(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def print_pattern3(n):
    for i in range(1, n + 1):
        print('* ' * 5)
   

def main():
    print("Pattern 1:")
    print_pattern1(2)
    print() # This line is added to keep a extra space between the 2 patterns (optional)
    print_pattern1(5)
    print() # This line is added to keep a extra space between the 2 patterns (optional)

    print("Pattern 2:")
    print_pattern2(2)
    print() # This line is added to keep a extra space between the 2 patterns (optional)
    print_pattern2(5)
    print() # This line is added to keep a extra space between the 2 patterns (optional)

    print("Pattern 3:")
    print_pattern3(2)
    print() # This line is added to keep a extra space between the 2 patterns (optional)
    print_pattern3(5)

if __name__ == "__main__":
    main()
