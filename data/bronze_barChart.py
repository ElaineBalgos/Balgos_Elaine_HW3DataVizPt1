import matplotlib.pyplot as plt
import numpy as np

years = [1924,1964,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
men = [4,1,4,4,1,2,5,0,4,1,5,7,3,7]
women = [0,0,0,0,0,0,0,1,5,4,1,5,3,10]
ind = [x for x, _ in enumerate(years)]

plt.bar(ind, men, width=0.9, label='Men', color='blue')
plt.bar(ind, women, width=0.9, label='Women', color='yellow')

plt.xticks(ind,years)
plt.xlabel("Years")
plt.ylabel("Men and Women Participants")
plt.legend(loc="upper right")
plt.title("Image 3.2, Bar Chart, Men and Women won Bronze Medal")

plt.show()