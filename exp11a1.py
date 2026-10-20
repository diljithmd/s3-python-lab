# Class names should start with a capital letter (e.g., Student)
class Student():
    def __init__(self, fname, lname, age, cpsm):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.cpsm = cpsm  # Store the mark as part of the student

    # 'print_details' method without using f-strings
    def print_details(self):
        # We pass each item as a separate argument to print()
        # It automatically adds spaces between them.
        print("Name:", self.fname, self.lname,self.age,self.cpsm)
        
# Get all the inputs from the user
fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
age = int(input("Enter the age: "))
cpsm = int(input("Enter the C++ mark: "))

# Create ONE student object with all four pieces of information
x = Student(fname, lname, age, cpsm)

# Call the single method to print all details
x.print_details()