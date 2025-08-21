import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# User input
user_input = input("Enter city names (comma-separated): ")
cities = [city.strip() for city in user_input.split(',') if city.strip()]

API_Key = '9788380b37fdd1f074df9f28c1ddc098'

# Prepare lists to store data
weather_data = []

# Fetch weather for each city
for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            'City': city,
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity']
        })
    else:
        print(f" Failed to get data for {city}: {response.json().get('message')}")

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# If no valid data, exit
if df.empty:
    print("No weather data was retrieved. Please check the city names and try again.")
    exit()

print("\n Weather Data:")
print(df)

# ---- Visualization using Seaborn ----
# Melt the DataFrame for grouped bar plot
df_melted = df.melt(id_vars='City', var_name='Metric', value_name='Value')

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='City', y='Value', hue='Metric', data=df_melted, marker='o')
plt.title('Temperature and Humidity in Selected Cities')
plt.ylabel('Value')
plt.xlabel('City')
plt.grid(True)
plt.tight_layout()
plt.show()
