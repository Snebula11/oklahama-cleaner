import pandas as pd


def pretty_print(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
