from dash import dcc
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd

from app import *
from components import header, fixed_row
from functions import *


ativo_org = {}
try:
    df_book = pd.read_csv('book_data.csv', index_col=0)
    ativo_org = iterar_sobre_df_book(df_book)
except:
    df_book = pd.DataFrame(columns=['date', 'preco', 'tipo', 'ativo', 'echange', 'vol', 'valor_total'])

try:
    df_historical_data = pd.read_csv('historical_data.csv', index_col=0)
except:
    df_historical_data = pd.DataFrame(columns=['datetime', 'symbol', 'close'])

df_historical_data = atualizar_historical_data(df_historical_data, ativo_org)

app.layout = dbc.Container([
    dcc.Location(id='url'),
    dcc.Store(id='book_data_store', data=df_book, storage_type='memory'),
    dcc.Store(id='historical_data_store', data=df_historical_data, storage_type='memory'),
    dcc.Store(id='layout_data', data=[], storage_type='memory'),
])