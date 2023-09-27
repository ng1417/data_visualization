import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('this_year_data_neighborhood.csv')  # Replace with your CSV file's path

# Filter out September data
df['Opened'] = pd.to_datetime(df['Opened'])  # Convert the 'Date' column to datetime if it's not already
df = df[~((df['Opened'].dt.month == 9))]  # Filter out rows where the month is September

# Group the data by 'Neighborhood' and count the occurrences
neighborhood_counts = df['Neighborhood'].value_counts()

# Combine neighborhoods with counts under a threshold into "Other"
threshold = 20000
neighborhoods_to_combine = neighborhood_counts[neighborhood_counts < threshold].index

# Use 'apply' to update the 'Neighborhood' column
df['Neighborhood'] = df['Neighborhood'].apply(lambda x: 'All Other Neighborhoods' if x in neighborhoods_to_combine else x)

# Recalculate neighborhood counts after combining
neighborhood_counts = df['Neighborhood'].value_counts()

# Sort the neighborhoods to ensure 'Other' appears last
neighborhood_counts = neighborhood_counts.sort_values(ascending=True)

# Create a bar chart
lighter_color = '#66b3ff' 
plt.figure(figsize=(10, 6))
#bars = plt.bar(neighborhood_counts.index, neighborhood_counts.values)
bars = plt.bar(neighborhood_counts.index, neighborhood_counts.values, color=lighter_color)


# Add labels and title

plt.title('Total 311 Requests by Neighborhood in San Francisco, CA \n January 1, 2023 - August 31, 2023')

# Rotate x-axis labels for better readability (optional) - more readible horizontal, just leaving in for reference.
#plt.xticks(rotation=45, ha='right')

# Add total counts inside each bar
for bar, count in zip(bars, neighborhood_counts.values):
    plt.text(bar.get_x() + bar.get_width() / 2, count / 2, str(count), ha='center', va='center')

# Remove the border/frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.yticks([])

# Show the chart
plt.tight_layout()
plt.show()
