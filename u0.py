import math
import numpy as np

def u0(f, arg):
	return f(arg)

#print(u0(lambda x: math.sin(x), 5))

initial_data = []
n = 51
x0 = 0
x = math.pi
#################################################################

h = (x - x0)/(n - 1)
for i in range(n):
	#print(i, end = ' ')
	initial_data.append(u0(lambda x: math.sin(x), x0 + i*h)) 

##################################################################
#print(np.array(initial_data, dtype = np.float64))
u = np.array(initial_data, dtype = np.float64)
print("The size of array ", u.size)
#Writing to the file
with open('u0.txt', mode = 'w') as g:
	for i in range(0, u.size):
		g.write(str(u[i]))
		g.write(' ')
	#g.close()
