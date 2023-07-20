class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Balance Available:", self.balance)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated: $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_details()



account_name = input("Add an user name in the bank database: ")
account_age = input('Add the user age: ')
account_gender = input("Add the user gender: ")
account = Bank(account_name, account_age, account_gender)

condition = True
while condition:
    choice = input('''Welcome to our online banking system!
0 - to deposit an amount of money
1 - to withdraw an amount of money
2 - to view the balance
Type 'quit' to exit.
Enter your choice: ''')
    
    if choice == '0':
        # Deposit Money Option Selected
        print()
        amount = int(input('Enter the amount you want to deposit: '))
        account.deposit(amount)
        print()
    elif choice == '1':
        # Withdraw Money Option Selected
        print()
        amount = int(input('Enter the amount you want to withdraw: '))
        account.withdraw(amount)
        print()
    elif choice == '2':
        # View Balance Option Selected
        print()
        account.view_balance()
        print()
    elif choice.lower() == 'quit':
        choice = str(input("Are you sure you want to quite the program? (yes/no): "))
        if choice == 'yes':
            print("Exiting the banking system. Goodbye!")
            condition=False
        if choice == 'no':
            continue
        
    else:
        print()
        print("Invalid choice. Please try again.")
        
    