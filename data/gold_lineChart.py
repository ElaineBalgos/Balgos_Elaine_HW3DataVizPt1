import matplotlib.pyplot as plt

years = [1968,1972,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
men = [1,1,1,4,0,0,0,1,7,1,6,6]
women = [0,0,0,0,0,3,2,1,0,1,2,10]

plt.plot(years, men, color=(255/255, 100/255, 100/255), linewidth=3.0)
plt.plot(years, women, color=(125/255, 100/255, 100/255), linewidth=3.0)

plt.ylabel("Years")
plt.xlabel("Men and Women Participants")
plt.title("Image 1.2 Line Chart, Men and Women won Gold Medals", pad=20)

# show the chart
plt.show()