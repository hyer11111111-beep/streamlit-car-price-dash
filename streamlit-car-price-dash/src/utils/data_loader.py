import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_data_summary(data):
    """Return a summary of the dataset."""
    if data is not None:
        return data.describe()
    return None

def load_and_process_data(file_path):
    """Load and process the data."""
    data = load_data(file_path)
    if data is not None:
        # Additional processing can be added here
        return data
    return None