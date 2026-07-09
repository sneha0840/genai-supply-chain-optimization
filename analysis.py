import pandas as pd

# Load dataset
df = pd.read_csv('trendvibe_data.csv')

# Estimate cost leakage: $45 per return, $8 per support ticket
df['Returns_Count'] = (df['Shipped_Orders'] * df['Return_Rate_Pct'] / 100).round(0)
df['Return_Cost'] = df['Returns_Count'] * 45
df['Support_Cost'] = df['Support_Tickets'] * 8
df['Total_Leakage'] = df['Return_Cost'] + df['Support_Cost']

print(f"Total Annual Cost Leakage: ${df['Total_Leakage'].sum():,.0f}\n")

# Correlation between Return Rate and Inventory Holding Cost
correlation = df['Return_Rate_Pct'].corr(df['Inventory_Holding_Cost_USD'])
print(f"Correlation (Return Rate vs. Inventory Holding Cost): {correlation:.2f}\n")

# Top 3 months by cost leakage
top_leakage = df.sort_values('Total_Leakage', ascending=False).head(3)
print("Top 3 Months by Cost Leakage:")
print(top_leakage[['Month', 'Total_Leakage']].to_string(index=False))
