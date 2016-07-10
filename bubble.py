bubble = [9,8,7,6,5,4,3,2,1]
def sorter(y):
	for i, j in enumerate(y[:-1]):
		if y[i] == y[len(y)-1]:
			continue
		elif j  > y[i+1]: 
			y[i],y[i+1] = y[i+1], y[i]
	print y

hundred = []

for i in range(100):
	import random
	hundred.append(random.randint(0,10000))
print hundred

for y in range(len(hundred)):
	print sorter(hundred)


