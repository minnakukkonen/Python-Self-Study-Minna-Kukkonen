import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load and clean the data
data = pd.read_csv('epa-sea-level.csv')
data.columns = data.columns.str.strip()
data = data[['Year', 'CSIRO Adjusted Sea Level']]
data = data.dropna()

# Create scatter plot of original data
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s=10, label='Original Data')

# First line of best fit (1880 - present)
slope1, intercept1, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
years_full = list(range(1880, 2051))
sea_level_full = [slope1 * year + intercept1 for year in years_full]
plt.plot(years_full, sea_level_full, color='red', label='Best Fit Line (1880-present)')

# Second line of best fit (2000 - present)
recent_data = data[data['Year'] >= 2000]
slope2, intercept2, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
years_recent = list(range(2000, 2051))
sea_level_recent = [slope2 * year + intercept2 for year in years_recent]
plt.plot(years_recent, sea_level_recent, color='green', label='Best Fit Line (2000-present)')

# Labels, title, legend, grid
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.xlim(1880, 2050)

# Display the plot
plt.show()