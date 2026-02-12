import pandas as pd

data = pd.read_csv("coffee_shop_sales.csv")

print(data.head(10))
print(data.tail())

print(data.info())
print(data.describe())

print(data["store_location"])
print(data[["unit_price", "product_category"]].head(10))

print(data.iloc[1050])
data.loc['unit_price'] > 3.0
print(data.loc[data["unit_price"] > 3.0])

# check missing data from dataset
print(data.isna())

# replace missing data from dataset
data.fillna(data["unit_price"].min(), inplace=True)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load only necessary columns to save memory
df = pd.read_csv('data.csv', usecols=['UnitPrice', 'Quantity', 'Category'])

# 2. Calculate total amount per row (Vectorized)
df['TotalAmount'] = df['UnitPrice'] * df['Quantity']

# 3. Aggregate data before plotting (Crucial for large datasets)
# Plotting millions of raw points is slow; plot summaries instead.
category_totals = df.groupby('Category')['TotalAmount'].sum()

# 4. Plot using Matplotlib
category_totals.plot(kind='bar')
plt.title('Total Amount by Category')
plt.ylabel('Amount ($)')
plt.show()