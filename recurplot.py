import matplotlib.pyplot as plt

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
	y_nodupe = [x for i, x in enumerate(y) if i==0 or x!=y[i-1]]

	#Plotting
	plt.plot(y_nodupe, '-o')
	plt.xlabel('Stack Step')
	plt.ylabel('X Value')
	plt.show()

	return y, y_nodupe