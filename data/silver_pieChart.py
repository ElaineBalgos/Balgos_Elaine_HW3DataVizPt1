import csv
import matplotlib.pyplot as plt

labels = 'men', 'women'
sizes = [37, 15]
colors = ['yellowgreen','lightskyblue']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Image 2.2 Line Chart, Men and Women won Silver Medals", pad=20)
plt.axis('equal')
plt.show()