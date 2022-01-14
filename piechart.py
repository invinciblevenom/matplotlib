import matplotlib.pyplot as plt
job_data = ['40', '20', '17', '8', '5', '10']
labels = 'IT', 'Finance', 'Marketing', 'Admin', 'HR', 'Operations'
explode = (0.25, 0, 0, 0, 0, 0)
plt.pie(job_data, labels=labels, explode=explode)
plt.show()
