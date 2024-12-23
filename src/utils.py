import pandas as pd

def load_csv(file_path):
    """Loads a CSV file and returns a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None