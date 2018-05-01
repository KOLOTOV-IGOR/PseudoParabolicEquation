import numpy as np
import math

def u0(f, arg):
	return f(arg)

class Grid:
	def __init__(self, nx, nt, lb, rb, T):
		#self.T  = T
		self.hx = (rb - lb)/nx
		self.ht = T/nt
		self.u0 = np.array(self.fill_u0(nx, lb), dtype = np.float64)

	def fill_u0(self, nx, lb):
		initial_data = []
		for i in range(nx+1):
			initial_data.append(u0(lambda x: math.sin(x), lb + i*self.hx))
		return initial_data

	def show(self):
		print(self.u0)
		print(self.hx, self.ht)
		print(len(self.u0))

