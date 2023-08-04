import numpy as np

# Quarterly sales data for the year
sales_q1 = np.array([100000, 120000, 130000])  # Sales for Q1 (in dollars)
sales_q2 = np.array([110000, 125000, 140000])  # Sales for Q2 (in dollars)
sales_q3 = np.array([120000, 135000, 150000])  # Sales for Q3 (in dollars)
sales_q4 = np.array([130000, 145000, 160000])  # Sales for Q4 (in dollars)

# Calculate total sales for the year
total_sales = sales_q1 + sales_q2 + sales_q3 + sales_q4

# Sum up the total sales for the year
total_sales_year = np.sum(total_sales)

# Calculate percentage increase from Q1 to Q4
percentage_increase = ((sales_q4 - sales_q1) / sales_q1) * 100
percentage_increase_year = np.mean(percentage_increase)  # Calculate the average increase across all categories

# Print the results
print("Total sales for the year:", total_sales_year)
print("Percentage increase from Q1 to Q4:", percentage_increase_year)
