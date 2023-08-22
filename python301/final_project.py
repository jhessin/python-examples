#!python3

"""
A simple banking app for managing deposits and withdrawals.
    # Class Based
    # Withdrawal and Deposit
    # Write the transaction to a python file
    #
    # Use:
    #     while True:
    # input
    # classes
    # methods
    # properties
"""


from typing import List
import pickle
import os
import sys

from errors_and_exceptions import getNum

GZIP_MAGIC = b"\x1F\x8B"


class ZeroTransactionError(Exception):
    pass


class Transaction:
    value: float
    description: str

    def __init__(self, value: float, description: str = '') -> None:
        if not value:
            raise ZeroTransactionError
        self.value = value
        self.description = description

    @property
    def isDeposit(self):
        return self.value > 0

    @property
    def isWithdrawal(self):
        return self.value < 0


class Account:
    _start_amount: float
    transactions: List[Transaction]
    name: str

    def __init__(self, name: str) -> None:
        """
        Initialize the account from a file if the name is a filename.
        Otherwise generate a new one.
        """
        self.name = name
        try:
            with open(f"{name}.db", 'rb') as fh:
                self._start_amount = pickle.load(fh)
                self.transactions = pickle.load(fh)
        except (EnvironmentError, pickle.PicklingError):
            print('Account not found!')
            self._start_amount = getNum('Starting amount', 0)
            self.transactions = []

    @property
    def amount(self):
        result = self._start_amount
        for t in self.transactions:
            result += t.value
        return result

    def deposit(self, t: Transaction):
        if t.isWithdrawal:
            return
        self.transactions.append(t)

    def withdraw(self, t: Transaction):
        if t.isDeposit:
            return
        self.transactions.append(t)

    def showTransactions(self):
        amount = self._start_amount
        print(f"-------{self.name}-------")
        print(f"Start amount: \t{self._start_amount}")
        print("============================")
        for t in self.transactions:
            amount += t.value
            print(f"""
{t.value} --- {amount}
\t{t.description if t.description else 'No description'}
                  """)
        print("============================")
        print(f"Final amount: \t{amount}")

    def export(self):
        fh = None
        try:
            with open(f"{self.name}.db", 'wb') as fh:
                pickle.dump(self._start_amount, fh, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.transactions, fh, pickle.HIGHEST_PROTOCOL)
                return True
        except (EnvironmentError, pickle.PicklingError) as err:
            print(f"{os.path.basename(sys.argv[0])}: export error: {err}")
            return False


def getTransaction() -> Transaction:
    amount = getNum('How much? ', 0)
    description = input('Description[optional]? ')
    return Transaction(amount, description)


def main():
    account_name = input("What is your account name? ")

    account = Account(account_name)

    while True:
        print("""
              What would you like to do?
              [1] New Transaction
              [2] View Report
              ==========================
              [q] Quit
              """)
        cmd = input('-> ').lower()
        if '1' in cmd:
            try:
                account.transactions.append(getTransaction())
            except ZeroTransactionError:
                continue
        elif '2' in cmd:
            account.showTransactions()
        elif 'q' in cmd:
            break
        else:
            print('Invalid Command. Try again.')

    account.export()


if __name__ == "__main__":
    main()
