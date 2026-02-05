# largestOfThree.py
try:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    c = int(input("Enter third integer: "))

    if a > b:
        if a > c:
            largest = a
        else:
            largest = c
    else:
        if b > c:
            largest = b
        else:
            largest = c

    print("The largest number is:", largest)

except ValueError:
    print("Error: Please enter integers only.")
