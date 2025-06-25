class BankAccount:
    def __init__(self):
        # Private attribute
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
account = BankAccount()
account.deposit(5000)
account.withdraw(2000)
account.check_balance()

