
from ibapi.contract import Contract
from fintech_ibkr import *

value = "EUR.USD" # This is what your text input looks like on your app

# Create a contract object
contract = Contract()
contract.symbol = value.split(".")[0]
contract.secType  = 'CASH'
contract.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
contract.currency = value.split(".")[1]

import sys
sys.stdout.write('wadup')
sys.stdout.flush()

# Get your contract details
contract_details = fetch_contract_details(contract)

str(contract_details).split(",")[10]

contract_details

print(contract_details)

# This script is an excellent place for scratch work as you figure this out.