class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"  # Default pin
        self.attempts = 3  # Number of allowed attempts

    def authenticate(self):
        """Authenticate user with a pin."""
        while self.attempts > 0:
            entered_pin = input("Enter your pin: ")
            if entered_pin == self.pin:
                print("Authentication successful!")
                return True
            else:
                self.attempts -= 1
                print(f"Incorrect pin. You have {self.attempts} attempts left.")
        print("Too many incorrect attempts. Exiting the system.")
        return False

    def check_balance(self):
        """Display the balance."""
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        """Deposit money into the ATM."""
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Deposit amount must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

    def withdraw(self):
        """Withdraw money from the ATM."""
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= self.balance:
                if amount > 0:
                    self.balance -= amount
                    print(f"Withdrew ${amount}. Your new balance is ${self.balance}.")
                else:
                    print("Withdrawal amount must be greater than 0.")
            else:
                print("Insufficient balance!")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

    def main_menu(self):
        """Main menu of the ATM."""
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Please select an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option! Please choose a valid number (1-4).")

if __name__ == "__main__":
    atm = ATM()
    if atm.authenticate():
        atm.main_menu()
