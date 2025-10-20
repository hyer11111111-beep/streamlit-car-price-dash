import pytest
import joblib
import pandas as pd
from src.pages.ml import run_ml

@pytest.fixture
def load_model():
    model = joblib.load('./model/regressor.pkl')
    return model

def test_model_prediction(load_model):
    test_data = pd.DataFrame({
        'Gender': [0],  # Female
        'Age': [30],
        'Annual Salary': [50000],
        'Credit Card Debt': [2000],
        'Net Worth': [100000]
    })
    
    prediction = load_model.predict(test_data)
    assert prediction.shape == (1,)
    assert prediction[0] >= 0  # Ensure the prediction is non-negative

def test_invalid_input(load_model):
    test_data = pd.DataFrame({
        'Gender': [1],  # Male
        'Age': [25],
        'Annual Salary': [30000],
        'Credit Card Debt': [-1000],  # Invalid negative debt
        'Net Worth': [50000]
    })
    
    with pytest.raises(ValueError):
        load_model.predict(test_data)