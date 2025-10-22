#!/usr/bin/env python3
#!/usr/bin/env python3
def valid (c):
    if c < 0:
        return False
    elif c > 0:
        return True
    else:
        return False

def fibonacci(num):
    list = []
    if num == 0:
        list.append(0)
    if num == 1:
        list.append(0)
        list.append(1)
    if num > 2:
        first, second = 0, 1
        list.append(first), list.append(second)
        for _ in range(2, num):
            total = first + second
            list.append(total)
            first, second = second, total
    return list

def printing(list):
    for i in list:
        print(i, end=" ")

def main ():
    while True:
        choice = int(input("Enter a number\n"))
        if valid(choice):
            break
        else:
            print("Enter a postive number\n")
    list = fibonacci(choice)
    printing(list)
    print("\n")

main()


# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
