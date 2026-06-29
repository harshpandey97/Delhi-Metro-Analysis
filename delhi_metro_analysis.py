# Delhi Metro Analysis
# Author: Harsh Pandey
# GitHub: github.com/HARSHPANDEY9756

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('delhi_metro_data.csv')

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic Stats:")
print(df.describe())

# =====================
# PLOT 1: Top 10 Busiest Stations
# =====================
plt.figure(figsize=(12,6))
top10 = df.nlargest(10, 'daily_passengers')
sns.barplot(x='daily_passengers', y='station_name', data=top10, palette='Blues_r')
plt.title('Top 10 Busiest Delhi Metro Stations', fontsize=16)
plt.xlabel('Daily Passengers')
plt.ylabel('Station Name')
plt.tight_layout()
plt.savefig('top10_busiest_stations.png')
plt.show()
print("Plot 1 saved!")

# =====================
# PLOT 2: Line-wise Passenger Load
# =====================
plt.figure(figsize=(10,6))
line_data = df.groupby('line')['daily_passengers'].sum().reset_index()
sns.barplot(x='line', y='daily_passengers', data=line_data, palette='Set2')
plt.title('Total Daily Passengers by Metro Line', fontsize=16)
plt.xlabel('Metro Line')
plt.ylabel('Total Daily Passengers')
plt.tight_layout()
plt.savefig('linewise_passengers.png')
plt.show()
print("Plot 2 saved!")

# =====================
# PLOT 3: Peak Hour Comparison
# =====================
plt.figure(figsize=(12,6))
df_peak = df[['station_name','peak_morning','peak_evening']].nlargest(10, 'peak_morning')
x = range(len(df_peak))
plt.bar(x, df_peak['peak_morning'], width=0.4, label='Morning Peak', color='steelblue')
plt.bar([i+0.4 for i in x], df_peak['peak_evening'], width=0.4, label='Evening Peak', color='coral')
plt.xticks([i+0.2 for i in x], df_peak['station_name'], rotation=45, ha='right')
plt.title('Morning vs Evening Peak — Top 10 Stations', fontsize=16)
plt.xlabel('Station')
plt.ylabel('Passengers')
plt.legend()
plt.tight_layout()
plt.savefig('peak_comparison.png')
plt.show()
print("Plot 3 saved!")

# =====================
# PLOT 4: Interchange vs Non-Interchange
# =====================
plt.figure(figsize=(8,6))
interchange_data = df.groupby('interchange')['daily_passengers'].mean().reset_index()
sns.barplot(x='interchange', y='daily_passengers', data=interchange_data, palette='coolwarm')
plt.title('Avg Daily Passengers — Interchange vs Non-Interchange', fontsize=16)
plt.xlabel('Interchange Station')
plt.ylabel('Avg Daily Passengers')
plt.tight_layout()
plt.savefig('interchange_analysis.png')
plt.show()
print("Plot 4 saved!")

print("\n✅ All Analysis Complete!")
print("4 plots saved as PNG files.")
