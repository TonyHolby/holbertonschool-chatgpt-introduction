#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self._display_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            self._display_balance()

    def _display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action == 'balance':
            cb._display_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

