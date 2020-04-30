#pie charts

import matplotlib.pyplot as plt

#x element
days = [1,2,3,4,5]

#y element
sleeping = [7,7,7,7,7]
eating = [1,2,1,3,2]
working = [8,7,8,7,6]
playing = [8,8,8,7,9]

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['cyan','b','r','orange']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        explode=[0,0.1,0.2,0],
        autopct='%1.1f%%')

###plotting format
plt.xlabel('x')
plt.ylabel('y')
plt.title('pie chart')
#plt.legend()
plt.show()
