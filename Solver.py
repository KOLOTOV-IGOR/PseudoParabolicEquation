#!/usr/bin/env python
from CLASS_GRID import Grid
import numpy as np
import scipy.linalg as la
import math

class Solver(Grid):
	def __init__(self, nx, nt, lb, rb, T, tau, eps, file_name):
		Grid.__init__(self, nx, nt, lb, rb, T)
		self.tau = tau
		self.eps = eps	
		self.res = np.zeros([(nx+1),(nt+1)], dtype = np.float64)
		
		alp = complex(0.5, 0.5)
		self.res[:,0] = self.u0[:]

		#F = np.zeros([2*nx-2, 1], dtype = np.float64)
		#Fu = np.zeros([2*nx-2, 2*nx-2], dtype = np.float64)
		M = self.fill_M(nx)
		U0 = self.fill_U0(nx)
		U = U0
		for i in range(1, nt+1):
			u = U
			F = self.fill_F(u, nx)
			Fu = self.fill_Fu(u, nx)
			A = M - alp*self.ht*Fu
			k = la.solve(A, F)
			U = U + self.ht*k.real
			self.res[1:nx,i] = U[:,0] #solution!
			#self.res[1:nx,i] = U[nx-1:2*nx-2,0]
		#np.savetxt(file_name, self.res, delimiter=" :: ")#"result.txt"

	def fill_M(self, nx):
		M = np.zeros([nx-1, nx-1], dtype = np.float64)
		for i in range(0, nx-1):
                	M[i][i] = -2/math.pow(self.hx, 2)
		for i in range(0, nx-2):
			M[i+1][i] = M[i][i+1] = 1/math.pow(self.hx, 2)
		return M

	def fill_U0(self, nx):
		U0 = np.zeros([nx-1, 1], dtype = np.float64)
		for i in range(1, nx):
			U0[i-1] = self.u0[i]
		return U0

	def fill_F(self, u, nx):
		F = np.zeros([nx-1, 1], dtype = np.float64)
		F[0] = -(math.exp(self.eps*u[0]) - 1)/self.tau - (u[1] - 2*u[0])/math.pow(self.hx,2)
		F[nx-2] = -(math.exp(self.eps*u[nx-2]) - 1)/self.tau - (- 2*u[nx-2] + u[nx-3])/math.pow(self.hx,2)
		for i in range(1, nx-2):
			F[i] = -(math.exp(self.eps*u[i]) - 1)/self.tau - (u[i+1] - 2*u[i] + u[i-1])/math.pow(self.hx,2)
		return F

	def fill_Fu(self, u, nx):
		Fu = np.zeros([nx-1, nx-1], dtype = np.float64)
		for i in range(0, nx-2):
			Fu[i+1][i] = Fu[i][i+1] = -1/math.pow(self.hx, 2)
		for i in range(0, nx-1):
			Fu[i][i] = 2/math.pow(self.hx, 2) - (self.eps/self.tau)*u[i]*math.exp(self.eps*u[i])
		return Fu

#eps = 2.1#input(float())
#tau = 2.01

#a = Solver(50, 50, 0, math.pi, 1, tau, eps, "test.txt")
#np.savetxt("test.txt", a.res[0:51:1, 0:51:1], delimiter=" :: ")


