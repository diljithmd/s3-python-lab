class Bank:
    def __init__(self, accountno, name, balance):
        self.accountno = accountno
        self.name = name
        self.balance = balance

    def add(self, amount):
        self.balance += amount
        print(f"After deposit, balance: {self.balance}")

    def remove(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"After withdrawal, balance: {self.balance}")

    def display(self):
        print("\nAccount Details:")
        print(f"Account No: {self.accountno}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("------")


# Create first account
acc_no1 = int(input("Enter account number for first user: "))
name1 = input("Enter name: ")
bal1 = float(input("Enter opening balance: "))
m1 = Bank(acc_no1, name1, bal1)

# Create second account
acc_no2 = int(input("\nEnter account number for second user: "))
name2 = input("Enter name: ")
bal2 = float(input("Enter opening balance: "))
m2 = Bank(acc_no2, name2, bal2)

# Perform transactions
m1.add(2000)
m2.remove(1000)

m1.add(5000)
m2.remove(3000)

# Display final account details
m1.display()
m2.display()