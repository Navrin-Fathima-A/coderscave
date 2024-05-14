import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
daily_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\daily_data.csv')
hourly_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\hourly_data.csv')
monthly_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\monthly_data.csv')
three_hour_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\three_hour_data.csv')

# Line plot for daily_data.csv
plt.figure(figsize=(10, 6))
plt.plot(daily_data['DATE'], daily_data['DailyAverageSeaLevelPressure'], color='blue')
plt.xlabel('DATE')
plt.ylabel('DailyAverageSeaLevelPressure (°C)')
plt.title('Daily Temperature Variation')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Line plot for monthly_data.csv
plt.figure(figsize=(10, 6))
monthly_data['DATE'] = pd.to_datetime(monthly_data['DATE']) # Convert 'Date' column to datetime
plt.plot(monthly_data['DATE'], monthly_data['MonthlyDepartureFromNormalAverageTemperature'], color='orange')
plt.xlabel('Date')
plt.ylabel('Average Monthly Mean Temperature (°F)')
plt.title('Average Monthly Mean Temperature Trend')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# KDE plot for three_hour_data.csv
plt.figure(figsize=(10, 6))
sns.kdeplot(three_hour_data['HourlyWindDirection'], color='red', shade=True)
plt.xlabel('Wind Direction')
plt.ylabel('Density')
plt.title('Temperature Distribution (Three-Hourly)')
plt.grid(True)
plt.show()
