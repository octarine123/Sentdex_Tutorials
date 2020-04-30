#stack plot

import matplotlib.pyplot as plt

#x element
days = [1,2,3,4,5]

#y element
sleeping = [7,7,7,7,7]
eating = [1,2,1,3,2]
working = [8,7,8,7,6]
playing = [8,8,8,7,9]

plt.plot([],[],color='m', label='sleeping')
plt.plot([],[],color='b', label='eating')
plt.plot([],[],color='r', label='working')
plt.plot([],[],color='orange', label='playing')


plt.stackplot(days, sleeping, eating, working, playing, colors=['m','b','r','orange'])

###plotting format
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()
