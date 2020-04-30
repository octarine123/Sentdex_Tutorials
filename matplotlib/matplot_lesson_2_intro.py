#barcharts/histograms
import matplotlib.pyplot as plt

#x = [2,4,6,8,10]
#y = [6,7,8,2,4]

#x2 = [1,3,5,7,9]
#y2 = [1,8,6,2,5]

#plt.bar(x, y, label='bar1', color='red')
#plt.bar(x2, y2, label='bar2', color='orange')

population_ages = [22,55,66,33,22,52,31,2,64,43,31,27,73,22,55,66,33,22,52,31,2,64,43,31,27,73]

ids = [x for x in range(len(population_ages)]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(populations_ages, bins, histtype='bar', rwidth=0)

###initial conditions/format
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Chart\nCheck it out')
plt.legend()
plt.show()
