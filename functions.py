import pandas as pd
import numpy as np
from pandas.tseries.offsets import DateOffset
from datetime import date 
from tvDatafeed import TvDatafeed

def iterar_sobre_df_book(df_book_var: pd.DataFrame, ativos_org_var = {}) -> dict:
    for _, row in df_book_var.iterrows():
        if not any (row['ativo'] in sublist for sublist in ativos_org_var):
            ativos_org_var[row['ativo']] = row['exchange']

    ativos_org_var['IBOV'] = 'BMFBOVESPA'
    return ativos_org_var

