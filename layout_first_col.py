
from dash import dcc
from dash import html
import dash_daq as daq

first_col = html.Div([
    # Section title
    html.H3("Section 1: Fetch & Display exchange rate historical data"),
    html.H4("Select value for whatToShow:"),
    html.Div(
        dcc.Dropdown(
            ["TRADES", "MIDPOINT", "BID", "ASK", "BID_ASK", "ADJUSTED_LAST",
             "HISTORICAL_VOLATILITY", "OPTION_IMPLIED_VOLATILITY",
             'REBATE_RATE', 'FEE_RATE', "YIELD_BID", "YIELD_ASK",
             'YIELD_BID_ASK', 'YIELD_LAST', "SCHEDULE"],
            "MIDPOINT",
            id='what-to-show'
        )
    ),
    html.H4("Select value for endDateTime:"),
    html.Div(
        children = [
            html.P(
                "You may select a specific endDateTime for the call to " + \
                "fetch_historical_data. If any of the below is empty, " + \
                "the current present moment will be used."
            )
        ]
    ),
    html.Div(
        children = [
            html.Div(
                children = [
                    html.Label('Date:'),
                    dcc.DatePickerSingle(id='edt-date')
                ],
                style = {
                    'display': 'inline-block',
                    'margin-right': '20px',
                }
            ),
            html.Div(
                children = [
                    html.Label('Hour:'),
                    dcc.Dropdown(list(range(24)), id='edt-hour'),
                ],
                style = {
                    'display': 'inline-block',
                    'padding-right': '5px'
                }
            ),
            html.Div(
                children = [
                    html.Label('Minute:'),
                    dcc.Dropdown(list(range(60)), id='edt-minute'),
                ],
                style = {
                    'display': 'inline-block',
                    'padding-right': '5px'
                }
            ),
            html.Div(
                children = [
                    html.Label('Second:'),
                    dcc.Dropdown(list(range(60)), id='edt-second'),
                ],
                style = {'display': 'inline-block'}
            )
        ]
    ),
    html.H4("Use RTH?"),
    html.Div(
        children=[
            daq.ToggleSwitch(
                id='use-rth',
                value=False
            )
        ]
    ),
    html.H4("Enter a currency pair:"),
    html.P(
        children=[
            "See the various currency pairs here: ",
            html.A(
                "currency pairs",
                href=('https://www.interactivebrokers.com/en/index.php?f'
                      '=2222&exch=ibfxpro&showcategories=FX')
            )
        ]
    ),
    # Currency pair text input, within its own div.
    html.Div(
        # The input object itself
        ["Input Currency: ", dcc.Input(
            id='currency-input', value='AUD.CAD', type='text'
        )],
        # Style it so that the submit button appears beside the input.
        style={'display': 'inline-block', 'padding-top': '5px'}
    ),
    # Submit button
    html.Button('Submit', id='submit-button', n_clicks=0),
    # Div for initial instructions and the updated info once submit is pressed
    html.Div(
        id='currency-output',
        children='Enter a currency code and press submit'),
],
    style={'width': '365px', 'display': 'inline-block'}
)
