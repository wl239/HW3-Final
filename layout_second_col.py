
from dash import dcc
from dash import html
import dash_daq as daq

second_col = html.Div([
    html.Div([
        html.H4(
            'Hostname: ',
            style={'display':'inline-block','margin-right':20}
        ),
        dcc.Input(
            id='default-host',
            value='127.0.0.01',
            type='text',
            style={'display':'inline-block'}
        ),
        html.H4(
            'Port: ',
            style={'display': 'inline-block', 'margin-right': 59}
        ),
        dcc.Input(
            id='default-port',
            value='7497',
            type='text',
            style={'display': 'inline-block'}
        ),
        html.H4(
            'Client ID: ',
            style={'display': 'inline-block', 'margin-right': 27}
        ),
        dcc.Input(
            id='default-clientid',
            value='10645',
            type='text',
            style={'display': 'inline-block'}
        )
    ]
    ),
    html.Br(),
    html.Button('CONNECT', id='connect-button', n_clicks=0),
    html.Div(id='connect-indicator')
],
    style={'width': '365px', 'display': 'inline-block'}
)