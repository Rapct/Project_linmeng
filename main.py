import passenger_analysis as pa

# Load and clean the data
file_path = 'passengers.csv'
df = pa.load_data(file_path)
cleaned_df = pa.clean_data(df)

print("First few rows of passenger data:")
print(cleaned_df.head())

# Calculate the average age for a specified travel class
travel_class = 'FIRST_CLASS'
loyalty_members = pa.calculate_average_age(cleaned_df, travel_class)
print(f"\nLoyalty members in {travel_class}:")
print(loyalty_members)

# Find loyalty members above a specified age
years = 50
experienced_members = pa.find_loyalty_members(cleaned_df, years)
print(f"\nLoyalty members with {years}+ years of experience:")
print(experienced_members)

# Get statistics for each travel class
class_stats = pa.get_class_statistics(cleaned_df)
print("\nStatistics for each travel class:")
print(class_stats)

# Plot and save age distribution chart
pa.plot_age_distribution(cleaned_df)
print("Age distribution chart saved as age_distribution.png")

# Plot and save bar chart for average age by travel class
pa.plot_average_age_by_class(cleaned_df)
print("Bar chart for average age by travel class saved as average_age_by_class.png")

# Plot and save scatter plot for age vs. loyalty membership
pa.plot_age_vs_loyalty(cleaned_df)
print("Scatter plot for age vs. loyalty membership saved as age_vs_loyalty.png")

# Plot and save box plot for age distribution by travel class
pa.plot_age_distribution_by_class(cleaned_df)
print("Box plot for age distribution by travel class saved as age_distribution_by_class.png")
