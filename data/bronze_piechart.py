import csv
import matplotlib.pyplot as plt

labels = 'men', 'women'
sizes = [48, 29]
colors = ['blue','green']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Image 3.1 Line Chart, Men and Women won Bronze Medals", pad=20)
plt.axis('equal')
plt.show()