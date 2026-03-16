
def find_largest(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("The largest value is:", largest)


num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
num3 = float(input("Enter third value: "))

find_largest(num1, num2, num3)