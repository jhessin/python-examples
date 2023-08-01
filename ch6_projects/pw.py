#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

def showUsage():
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

if len(sys.argv) < 2:
    showUsage()

account = sys.argv[1]      # first command line arg is the account name

if account not in PASSWORDS:
    print(account, 'not found')
    showUsage()

pyperclip.copy(PASSWORDS[account])
print('Password for', account, 'copied to clipboard.')
