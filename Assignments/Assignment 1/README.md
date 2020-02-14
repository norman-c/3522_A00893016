# Comp 3522 Assignment 1

Family Appointed Moderator program used to set budgets, record transactions, and view transactions of users.

## Features

Creating a user or using test user data available.

View Budgets

Record a Transaction

View Transaction by Budgets

View Bank Account Details

### How the application works

It will ask for user input on creating a user first (loading user data can also be selected here)

A menu will then be displayed for the user to select an option.

Viewing budgets is done by accessing the list of budget objects stored in the user object and printing them.

Recording a transaction is done the TransactionGen class and by asking the user for the nessecary parameters to create the transaction. It is then checked for if the user has the balance for it before appending to a list of transactions in the main class fam. Checks are also made here for lockout as well as if messages will be displayed to notify the user of exceeding budgets.

Viewing transactions by budget is done by asking the user for the budget to be viewed and then printing out the transactions for them.

Viewing bank account details accesses the user object and prints the bank details from within.


