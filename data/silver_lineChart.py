import matplotlib.pyplot as plt

years = [1968,1972,1980,1984,1994,1998,2002,2006,2010,2014]
men = [4,1,5,5,0,6,1,4,9,2]
women = [0,0,0,0,2,1,5,0,6,1]

plt.plot(years, men, color=(195/255, 100/255, 100/255), linewidth=3.0)
plt.plot(years, women, color=(25/255, 100/255, 100/255), linewidth=3.0)

plt.ylabel("Years")
plt.xlabel("Men and Women Participants")
plt.title("Image 2.1 Line Chart, Men and Women won Silver Medals", pad=20)

# show the chart
plt.show()