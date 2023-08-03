import pandas as pd

data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 5, 2, 6],
    'area_sqft': [1500, 1800, 2200, 1200, 2500],
    'listing_price': [250000, 300000, 350000, 200000, 400000]
}

# Create the DataFrame
property_data = pd.DataFrame(data)

# 1. The average listing price of properties in each location.
average_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. The number of properties with more than four bedrooms.
properties_with_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_with_more_than_four_bedrooms)

# 3. The property with the largest area.
property_with_largest_area = property_data[property_data['area_sqft'] == property_data['area_sqft'].max()]

print("Average listing price of properties in each location:")
print(average_price_by_location)

print("Number of properties with more than four bedrooms:")
print(num_properties_more_than_four_bedrooms)

print("Property with the largest area:")
print(property_with_largest_area)
