
from ibapi.contract import Contract
from ibapi.order import Order
import threading
from fintech_ibkr.ibkr_app import ibkr_app


hostname = '127.0.0.1'
port = 7497
client_id = 10645 # can set and use your Master Client ID

value = "EUR.USD" # This is what your text input looks like on your app

# Create a contract object
contract = Contract()
contract.symbol = value.split(".")[0]
contract.secType  = 'CASH'
contract.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
contract.currency = value.split(".")[1]

action = "BUY"
trade_amt = 10
order = Order()
order.action = action
order.orderType = "MKT"
order.totalQuantity = trade_amt

app = ibkr_app()
app.connect(hostname, port, client_id)
while not app.isConnected():
    time.sleep(0.01)

def run_loop():
    app.run()

api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

while isinstance(app.next_valid_id, type(None)):
    time.sleep(0.01)

app.placeOrder(app.next_valid_id, contract, order)

app.disconnect()


