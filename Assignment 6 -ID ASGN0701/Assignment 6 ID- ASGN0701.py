from typing import Protocol
import unittest

# Transaction Protocol
class Transaction(Protocol):
    def execute(self):
        pass


# Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def __str__(self):
        return f"{self.account_holder} Balance: {self.balance}"


# Deposit Transaction
class Deposit:
    def __init__(self, account: BankAccount, amount: float):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)
        print(f"Deposited {self.amount} to {self.account.account_holder}")


# Withdrawal Transaction
class Withdrawal:
    def __init__(self, account: BankAccount, amount: float):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)
        print(f"Withdrawn {self.amount} from {self.account.account_holder}")


# Transfer Transaction
class Transfer:
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def execute(self):
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Transferred {self.amount} from {self.from_account.account_holder} to {self.to_account.account_holder}")


# Demonstration
def run_demo():
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)

    transactions = [
        Deposit(acc1, 200),
        Withdrawal(acc1, 100),
        Transfer(acc1, acc2, 300)
    ]

    for transaction in transactions:
        transaction.execute()

    print(acc1)
    print(acc2)


# Unit Testing
class TestTransactions(unittest.TestCase):

    def test_deposit(self):
        acc = BankAccount("Test", 100)
        d = Deposit(acc, 50)
        d.execute()
        self.assertEqual(acc.balance, 150)

    def test_withdrawal(self):
        acc = BankAccount("Test", 100)
        w = Withdrawal(acc, 40)
        w.execute()
        self.assertEqual(acc.balance, 60)

    def test_transfer(self):
        acc1 = BankAccount("A", 200)
        acc2 = BankAccount("B", 100)
        t = Transfer(acc1, acc2, 50)
        t.execute()
        self.assertEqual(acc1.balance, 150)
        self.assertEqual(acc2.balance, 150)


if __name__ == "__main__":
    print("---- Demo Output ----")
    run_demo()

    print("\n---- Running Unit Tests ----")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
