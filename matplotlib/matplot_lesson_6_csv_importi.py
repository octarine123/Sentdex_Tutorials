#import csv data
import matplotlib.pyplot as plt
import numpy as np

#Part 1 csv method
''''
import csv
x = []
y = []

#with open('/home/pi/Documents/sentdex/matplotlib/example', 'r') as csvfile: #long path
with open('example', 'r') as csvfile: #short path
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='loaded from file')
'''

#part 2 numpy method

x,y =np.loadtxt('example', delimiter=',', unpack=True)

plt.plot(x,y,label='loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Stuff')
plt.show()
