import matplotlib.pyplot as plt
import numpy as np

def recurplot2(x,n):
	y=[]
	print(x,n)
	basecase = range(1,n+1)

	def recur(x):
		if x in basecase:
			y.append(x)
			return

		for i in range(1,n+1):
			y.append(x)
			recur(x-i)
			y.append(x)

	recur(x)
	
	
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