import matplotlib.pyplot as plt
import numpy as np

years = [1968,1972,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
men = [1,1,1,4,0,0,0,1,7,1,6,6]
women = [0,0,0,0,0,3,2,1,0,1,2,10]
ind = [x for x, _ in enumerate(years)]

plt.bar(ind, men, width=0.9, label='Men', color='green')
plt.bar(ind, women, width=0.9, label='Women', color='orange')

plt.xticks(ind,years)
plt.xlabel("Years")
plt.ylabel("Men and Women Participants")
plt.legend(loc="upper right")
plt.title("Image 1.1, Bar Chart, Men and Women won Gold Medal")

plt.show()