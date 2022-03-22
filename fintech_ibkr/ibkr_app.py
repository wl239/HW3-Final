
import pandas as pd
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from datetime import datetime

# This is the main app that we'll be using for sync and async functions.
class ibkr_app(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.error_messages = pd.DataFrame(columns=[
            'reqId', 'errorCode', 'errorString'
        ])
        self.next_valid_id = None
        self.current_time = None
        ########################################################################
        # Here, you'll need to change Line 30 to initialize
        # self.historical_data as a dataframe having the column names you
        # want to use. Clearly, you'll want to make sure your colnames match
        # with what you tell the candlestick figure to expect when you create
        # it in your app!
        # I've already done the same general process you need to go through
        # in the self.error_messages instance variable, so you can use that as
        # a guide.
        self.historical_data = pd.DataFrame(
            columns=['date', 'open', 'high', 'low', 'close', 'volume',
                     'bar_count', 'average']
        )
        self.historical_data_end = ''
        self.contract_details = ''
        self.contract_details_end = ''

    def error(self, reqId, errorCode, errorString):
        self.error_messages = pd.concat(
            [self.error_messages, pd.DataFrame({
                "reqId": [reqId],
                "errorCode": [errorCode],
                "errorString": [errorString]
            })])

    def managedAccounts(self, accountsList):
        self.managed_accounts = [i for i in accountsList.split(",") if i]

    def nextValidId(self, orderId: int):
        self.next_valid_id = orderId

    def currentTime(self, time:int):
        self.current_time = datetime.fromtimestamp(time)

    def historicalData(self, reqId, bar):
        # YOUR CODE GOES HERE: Turn "bar" into a pandas dataframe, formatted
        #   so that it's accepted by the plotly candlestick function.
        # Take a look at candlestick_plot.ipynb for some help!
        # assign the dataframe to self.historical_data.
        # print(reqId, bar)
        bar_df = pd.DataFrame(
            {
                'date': [bar.date],
                'open': [bar.open],
                'high': [bar.high],
                'low': [bar.low],
                'close': [bar.close],
            }
        )
        self.historical_data = pd.concat(
            [self.historical_data, bar_df],
            ignore_index=True
        )

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        self.historical_data_end = reqId

    def contractDetails(self, reqId: int, contractDetails):
        self.contract_details = contractDetails

    def contractDetailsEnd(self, reqId: int):
        self.contract_details_end = reqId