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


# Helper: Clean data
def clean_data(df):
    # Standardize column names
    df.columns = [col.strip().lower() for col in df.columns]
    # Remove rows with missing prices
    df = df[df['our_price'].notnull()]
    # Convert price to float (handle "$" sign)
    df['our_price'] = df['our_price'].replace('[\$,]', '', regex=True).astype(float)
    # Treat missing stock values as zero
    df['current_stock'] = pd.to_numeric(df['current_stock'], errors='coerce').fillna(0)
    return df

# Helper: Fetch currency exchange rates from Open Exchange Rates API
def fetch_exchange_rate(base_currency="USD", target_currency="EUR"):
    API_KEY = os.getenv("API_KEY")  # Load API key from .env
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rates = data["rates"]
            if target_currency in rates:
                return rates[target_currency]
            else:
                print(f"Currency {target_currency} not found in rates.")
                return None
        else:
            print(f"API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None