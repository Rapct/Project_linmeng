import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


# a) Load the data
def load_data(file_path):
    columns = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
    df = pd.read_csv(file_path, names=columns, header=0)
    return df


# b) Clean the data
def clean_data(df):
    # 将出生日期列转换为日期类型
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    
    # 确保忠诚会员列为布尔类型
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(bool)
    
    # 返回清理后的DataFrame
    return df


# Example: Load and clean the data
file_path = r"C:\Users\Mengtian Lin\Desktop\CPS3320\Project\Project_linmeng\passengers.csv"
df = load_data(file_path)
cleaned_df = clean_data(df)
print(cleaned_df.head())




###############################################################################
#Task 2: Decision Making and Loops (20 points) 

def calculate_average_age(df, travel_class):
    # Filter out passengers with the specified travel class
    filtered_df = df[df['TravelClass'].str.upper() == travel_class.upper()].copy()
    
    # Calculate age and add it to the dataframe
    current_year = pd.to_datetime('today').year
    filtered_df['Age'] = current_year - filtered_df['Birthdate'].dt.year
    
    # Return the names of loyalty members
    loyalty_members = filtered_df[filtered_df['LoyaltyMember']]['Name'].tolist()
    return loyalty_members




def find_loyalty_members(df, years):
    # Create a copy of the original DataFrame
    df_copy = df.copy()
    
    # Calculate age and add it to the copy DataFrame
    current_year = pd.to_datetime('today').year
    df_copy['Age'] = current_year - df_copy['Birthdate'].dt.year
    
    # Return the names of members with age greater than or equal to the specified years
    experienced_members = df_copy[df_copy['Age'] >= years]['Name'].tolist()
    return experienced_members




######################################
# Task 3: Functions and Modules
# a) Get class statistics
def get_class_statistics(df):
    # Calculate the age column
    current_year = pd.to_datetime('today').year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Initialize the result dictionary
    class_stats = {}
    
    # Get the unique travel classes
    travel_classes = df['TravelClass'].unique()
    
    for class_ in travel_classes:
        # Filter the data for the current travel class
        class_df = df[df['TravelClass'] == class_]
        
        # Calculate the average age
        average_age = class_df['Age'].mean()
        
        # Calculate the number of loyalty members
        loyalty_members = class_df['LoyaltyMember'].sum()
        
        # Store the results in the dictionary
        class_stats[class_] = {
            'Average Age': round(average_age, 2),
            'Loyalty Members': int(loyalty_members)
        }
    
    return class_stats

###############################################################################
# Task 4: Data Visualization with Matplotlib

def plot_age_distribution(df):
    # Calculate age
    current_year = pd.to_datetime('today').year
    df['Age'] = current_year - df['Birthdate'].dt.year

    # Plot age distribution histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=30, edgecolor='black')
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Number of Passengers')
    plt.grid(True)
    
    # Save the plot
    plt.savefig('age_distribution.png')
    plt.close()

def plot_average_age_by_class(df):
    # Calculate age
    current_year = pd.to_datetime('today').year
    df['Age'] = current_year - df['Birthdate'].dt.year

    # Calculate the average age for each travel class
    avg_age_by_class = df.groupby('TravelClass')['Age'].mean().sort_values()

    # Plot the bar chart for average age by travel class
    plt.figure(figsize=(10, 6))
    avg_age_by_class.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.xticks(rotation=45)
    plt.grid(True)
    
    # Save the plot
    plt.savefig('average_age_by_class.png')
    plt.close()



###############################################################################
# Task 5: Data Visualization with Seaborn and Plotly (20 points) 
def plot_age_vs_loyalty(df):
    # 计算年龄
    current_year = pd.to_datetime('today').year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # 使用Seaborn绘制散点图
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='LoyaltyMember', hue='TravelClass', style='TravelClass', s=100)
    plt.title('Age vs. Loyalty Membership')
    plt.xlabel('Age')
    plt.ylabel('Loyalty Membership (True/False)')
    plt.grid(True)
    
    # 保存图片
    plt.savefig('age_vs_loyalty.png')
    plt.close()



def plot_age_distribution_by_class(df):
    current_year = pd.to_datetime('today').year
    df.loc[:, 'Age'] = current_year - df['Birthdate'].dt.year

    # fig = px.box(df, x='TravelClass', y='Age', title='Age Distribution by Travel Class', labels={'TravelClass': 'Travel Class', 'Age': 'Age'})
    # fig.show()

    # Create a new graphic
    plt.figure(figsize=(10, 6))
    
    # Plotting box plots with seaborn
    sns.boxplot(x='TravelClass', y='Age', data=df)
    
    # Add title and tags
    plt.title('Age Distribution by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Age')
    
    # Save the graph and close the graph window
    plt.savefig('age_distribution_by_class.png')
    plt.close()

    
# def plot_age_distribution_by_class(df):
#     current_year = pd.to_datetime('today').year
#     df.loc[:, 'Age'] = current_year - df['Birthdate'].dt.year

#     fig = px.box(df, x='TravelClass', y='Age', title='Age Distribution by Travel Class', labels={'TravelClass': 'Travel Class', 'Age': 'Age'})
#     fig.write_image('age_distribution_by_class.png')  # 保存为图片文件

