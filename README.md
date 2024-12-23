# 10EQS Data Integration Challenge

## Description

This tool helps small business owners track product prices against market conditions. It integrates with the Open Exchange Rates API to convert prices into a target currency (e.g., EUR) and provides actionable insights.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd 10eqs-evaluation
2. Install dependencies:
3. Add your Open Exchange Rates API key:
    Create a .env file in the project root:
    API_KEY=your_openexchangerates_api_key
4. Run the analysis:
    python src/analysis.py data/products.csv