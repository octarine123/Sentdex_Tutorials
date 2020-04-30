#scatter plots

import matplotlib.pyplot as plt

x = range(8)
y = [5,2,5,7,2,7,9,11]

x2 = [1,2,3,4,5,6,7,8]
y2 = [3,1,10,11,15,2,19,3]


plt.scatter(x,y,label='scatter1', color='red',marker='o',s=14)
plt.scatter(x2,y2,label='scatter2', color='blue',marker='o',s=14)


###plotting format
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Graph')
plt.legend()
plt.show()
