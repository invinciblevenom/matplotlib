import matplotlib.pyplot as plt
import seaborn as sns
flight_data = sns.load_dataset('flights') 
flight_data.head()
flight_data = flight_data.pivot('month', 'year', 'passengers')
sns.heatmap(flight_data)
plt.show()
