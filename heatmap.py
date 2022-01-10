import matplotlib.pyplot as plt
import seaborn as sns
flight_data = sns.load_dataset('flight')
flight_data.head()
flight_data = flight_data.pivot('month', 'year', 'passengers')
flight_data
sns.heatmap(flight_data)
