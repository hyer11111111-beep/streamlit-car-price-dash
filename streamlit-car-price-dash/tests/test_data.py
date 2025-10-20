import pytest
import pandas as pd
from src.utils.data_loader import load_data
from src.utils.preprocessing import preprocess_data

def test_load_data():
    df = load_data('./data/Car_Purchasing_Data.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'Gender' in df.columns
    assert 'Age' in df.columns

def test_preprocess_data():
    df = load_data('./data/Car_Purchasing_Data.csv')
    processed_df = preprocess_data(df)
    assert 'Annual Salary' in processed_df.columns
    assert processed_df['Annual Salary'].isnull().sum() == 0
    assert processed_df['Credit Card Debt'].min() >= 0
    assert processed_df['Net Worth'].min() >= 0