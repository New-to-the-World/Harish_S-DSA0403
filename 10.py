import matplotlib.pyplot as plt

# Sample dataset containing month and sales values
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales_values = [15000, 18000, 22000, 25000, 28000, 30000]

# Create a line plot
plt.figure(figsize=(8, 5)) 
plt.plot(months, sales_values, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  
plt.xticks(rotation=45) 
plt.tight_layout()
plt.savefig('monthly_sales_line_plot.png')
plt.show()

# Create a bar plot
plt.figure(figsize=(8, 6))  
plt.bar(months, sales_values, color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True) 
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()
