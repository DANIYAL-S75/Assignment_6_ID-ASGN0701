# Assignment_6_ID-ASGN0701
Transaction Protocol Banking System
Overview

This project demonstrates the use of a Transaction Protocol in Python for a banking application. The system supports multiple types of transactions such as Deposit, Withdrawal, and Transfer.

By using a protocol, all transaction classes follow a common structure with an execute() method. This allows different transactions to be handled in a flexible and consistent way.

Features

Bank account management

Deposit money into an account

Withdraw money from an account

Transfer money between accounts

Transaction protocol using Python Protocol

Unit testing to verify transaction functionality

Technologies Used

Python 3

typing.Protocol

unittest module for testing

Project Structure
project_folder/
│
├── transaction_system.py   # Main Python program
└── README.md               # Project documentation
Classes Implemented
1. Transaction Protocol

Defines a common interface with the execute() method that every transaction must implement.

2. BankAccount

Represents a bank account with:

Account holder name

Account balance

Deposit and withdrawal methods

3. Deposit

Implements a transaction that adds money to a bank account.

4. Withdrawal

Implements a transaction that removes money from a bank account.

5. Transfer

Implements a transaction that transfers money from one account to another.

How to Run the Program

Install Python 3.

Save the code in a file named transaction_system.py.

Run the program using:

python transaction_system.py

The program will:

Execute sample transactions

Display account balances

Run unit tests
