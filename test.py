import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
        'Age': [25, 28, 32, 30],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Accessing columns
print(df['Name'])  # Access 'Name' column
print(df.Age)     # Access 'Age' column

# Filtering rows
filtered_df = df[df['Age'] > 28]  # Filter rows where 'Age' > 28
print(filtered_df)

# Adding a new column
df['Country'] = ['USA', 'UK', 'France', 'Japan']
print(df)

# Grouping and aggregating data
grouped_df = df.groupby('Country').mean()  # Group by 'Country' and calculate mean
print(grouped_df)