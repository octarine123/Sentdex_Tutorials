import matplotlib.pyplot as plt

x = [1,2,3] #function x
y = [4,2,6] #function y

x2 = [1,2,3] #function x
y2 = [4,6,12] #function y

plt.plot(x,y, label ='First Line') #line plot
plt.plot(x2,y2, label = 'Second line') #plot line 2
plt.xlabel('Plot Number')
plt.ylabel('Important Number')

plt.title('Graph 2\nCheck it out')
plt.legend()
plt.show()
