L = [5, 8, 2, 9]
try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    d = a / b
    print(0
     L)
    c = int(input("Enter index of element: "))
    print("Element at index", c, ":", L[c])

except IndexError:
    print("Index must be between 0 and 3")

except ValueError:
    print("Invalid data entered")

except ZeroDivisionError:
    print("Divisor should not be zero")
else:
    print("Division result:", d)