print('How many green bottles are sitting on the wall?')
i=1
for i in range (5):
    print(( str(i) ) + (' bottles sitting on the wall'))
    i= i +1

total = 0
for num in range(101):
    total = total + num
print(total)

del i
for i in range(5, -1, -1):
    print(i)
