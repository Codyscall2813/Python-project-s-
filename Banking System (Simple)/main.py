import random
import os

class Bank:
    def __init__(self):
        """Initializes a Bank object with dictionaries to store user accounts and transaction history."""
        self.user_accounts = {}
        self.transaction_history = {}

    def create_account(self, name, initial_deposit):
        """Creates a new bank account for a user.

        Args:
            name (str): The name of the account holder.
            initial_deposit (float): The initial balance for the account.

        Returns:
            BankAccount: The created BankAccount object.
        """
        account_id = self._generate_account_number()
        new_account = BankAccount(account_id, name, initial_deposit)
        self.user_accounts[account_id] = new_account
        self.transaction_history[account_id] = []
        return new_account

    def _generate_account_number(self):
        """Generates a random 8-digit account number.

        Returns:
            str: The generated account number.
        """
        return "".join(random.choice("0123456789") for _ in range(8))

    def get_account(self, account_id):
        """Retrieves a BankAccount object based on the account number.

        Args:
            account_id (str): The account number to look up.

        Returns:
            BankAccount: The BankAccount object if found, else None.
        """
        return self.user_accounts.get(account_id)

    def perform_transaction(self, account_id, transaction_type, amount):
        """Performs a transaction (deposit or withdrawal) on a user's account.

        Args:
            account_id (str): The account number for the transaction.
            transaction_type (str): The type of transaction (deposit or withdraw).
            amount (float): The transaction amount.

        Returns:
            str: A message indicating the result of the transaction.
        """
        account = self.get_account(account_id)
        if not account:
            return "Account not found."

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            if account.withdraw(amount):
                self.transaction_history[account_id].append((transaction_type, amount))
                return "Transaction completed."
            else:
                return "Insufficient funds."
        else:
            return "Invalid transaction type."

    def get_transaction_history(self, account_id):
        """Retrieves the transaction history for a user's account.

        Args:
            account_id (str): The account number to look up.

        Returns:
            list: A list of tuples representing transaction history (type, amount).
        """
        return self.transaction_history.get(account_id, [])

class BankAccount:
    def __init__(self, account_id, holder_name, balance):
        """Initializes a BankAccount object.

        Args:
            account_id (str): The account number.
            holder_name (str): The name of the account holder.
            balance (float): The initial balance for the account.
        """
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        """Deposits funds into the account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """Withdraws funds from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False if there were insufficient funds.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        """Retrieves the current balance of the account.

        Returns:
            float: The account balance.
        """
        return self.balance
    
    

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    """Main function to run the Python Banking System."""
    bank_name = "———Bank of Python———"
    bank = Bank()

    while True:
        clear_screen()
        print(f"{bank_name}")
        print("Personal Banking System")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            holder_name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            account = bank.create_account(holder_name, initial_deposit)
            print(f"Account created successfully. Account Number: {account.account_id}")

        elif choice == "2":
            account_id = input("Enter account number: ")
            transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
            amount = float(input("Enter transaction amount: "))
            result = bank.perform_transaction(account_id, transaction_type, amount)
            print(result)

        elif choice == "3":
            account_id = input("Enter account number: ")
            account = bank.get_account(account_id)
            if account:
                print(f"Account Balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "4":
            account_id = input("Enter account number: ")
            transactions = bank.get_transaction_history(account_id)
            if transactions:
                print("Transaction History:")
                for trans_type, amount in transactions:
                    print(f"{trans_type.capitalize()}: ${amount}")
            else:
                print("Account not found or no transaction history.")

        elif choice == "5":
            print("Exiting the Python Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
