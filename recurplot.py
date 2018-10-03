import matplotlib.pyplot as plt
import numpy as np

def recurplot(x,n):
	y=[]
	print(x,n)

	def recur(x):
		if x==0:
			#print(x)
			y.append(0)
			return

		for i in range(n):
			y.append(x)
			#print(x)
			recur(x-1)
			#print(x)
			y.append(x)
	
	recur(x)
	
	#still have to remove adjacent duplicates
	#Use arrays to make this easier
	mask=np.diff(y)==0
	mask=np.append(mask,False) #Match index sizes
	mask=np.where(mask)[0] #Return index locations of "True", normally returns a tuple

	y=np.delete(y,mask)

	#Plotting
	plt.plot(y, '-o')
	plt.xlabel('Stack Step')
	plt.ylabel('X Value')
	plt.show()

	return y

