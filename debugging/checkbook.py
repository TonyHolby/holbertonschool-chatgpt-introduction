#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        """Initialize the checkbook with zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit money into the checkbook."""
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self._display_balance()

    def withdraw(self, amount):
        """Withdraw money from the checkbook."""
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
        """Display the current balance."""
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    """Main function to interact with the checkbook."""
    cb = Checkbook()  # Create a new instance of the Checkbook class
    while True:
        # Prompt the user for action (deposit, withdraw, balance, exit)
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)  # Call deposit method
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)  # Call withdraw method
        elif action == 'balance':
            cb._display_balance()  # Call _display_balance method
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()  # Start the main function

