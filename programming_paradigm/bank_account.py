#!/usr/bin/env python3
"""
Defines the BankAccount class to demonstrate OOP principles like
encapsulation and methods.
"""

class BankAccount:
    """
    Represents a simple bank account with basic deposit, withdrawal,
    and balance display functionality.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance.
        
        Args:
            initial_balance (float): The starting balance of the account. Defaults to 0.0.
        """
        # Encapsulation: The balance is managed internally by the methods.
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")

# End of bank_account.py