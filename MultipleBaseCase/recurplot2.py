import matplotlib.pyplot as plt

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
	
	#still have to remove adjacent duplicates
	y_nodupe = [x for i, x in enumerate(y) if i==0 or x!=y[i-1]]

	#Plotting
	plt.plot(y_nodupe, '-o')
	plt.xlabel('Stack Step')
	plt.ylabel('X Value')
	plt.show()

	return y, y_nodupe