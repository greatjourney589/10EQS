import sys
from utils import load_csv, clean_data, fetch_exchange_rate

def analyze_products(csv_path):
    # Step 1: Load the CSV data
    print("Loading product data...")
    data = load_csv(csv_path)
    if data is None:
        print("Failed to load data. Exiting.")
        return
    
    # Step 2: Clean the data
    print("Cleaning product data...")
    cleaned_data = clean_data(data)
    
    # Step 3: Fetch exchange rate (USD to EUR in this example)
    print("Fetching exchange rate...")
    exchange_rate = fetch_exchange_rate(base_currency="USD", target_currency="EUR")
    if exchange_rate is None:
        print("Failed to fetch exchange rate. Exiting.")
        return

    # Step 4: Generate insights
    print("Generating insights...")
    insights = []
    for index, row in cleaned_data.iterrows():
        # Convert "our_price" to EUR
        price_in_eur = row['our_price'] * exchange_rate
        insights.append({
            "product": row['product_name'],
            "our_price_usd": row['our_price'],
            "our_price_eur": round(price_in_eur, 2),
            "current_stock": row['current_stock']
        })

    # Step 5: Generate report
    print("Writing report...")
    with open("report.md", "w") as report_file:
        report_file.write("# Product Analysis Report\n\n")
        report_file.write("## Exchange Rate\n")
        report_file.write(f"- 1 USD = {exchange_rate} EUR\n\n")
        report_file.write("## Key Insights\n")
        for insight in insights:
            report_file.write(f"- **{insight['product']}**:\n")
            report_file.write(f"  - Price (USD): ${insight['our_price_usd']}\n")
            report_file.write(f"  - Price (EUR): €{insight['our_price_eur']}\n")
            report_file.write(f"  - Current Stock: {insight['current_stock']}\n\n")
    
    print("Report generated: report.md")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/analysis.py <path_to_csv>")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    analyze_products(csv_path)