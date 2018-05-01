#!/usr/bin/env python
import Solver as S
import numpy  as np
import math

def eff_order(nx, nt, u1, u2, u3):
	p_eff = np.zeros([(nx),(nt)], dtype = np.float64)
	u_num = u2 - u1
	u_den = u3 - u2
	#print(np.shape(u_num))
	#print(np.shape(u_den))
	for i in range(0, nx):
		for j in range(0, nt):
			p_eff[i][j] = math.log(abs(u_num[i][j])/abs(u_den[i][j]), 2)

	return p_eff

eps = 2.1#input(float())
tau = 2.01

a = S.Solver(50, 50, 0, math.pi, 1, tau, eps, "result.txt")
b = S.Solver(2*50, 2*50, 0, math.pi, 1, tau, eps, "2result.txt")
c = S.Solver(4*50, 4*50, 0, math.pi, 1, tau, eps, "4result.txt")

np.savetxt("res1.txt", a.res[0:51:1, 0:51:1], delimiter=" :: ")
np.savetxt("res2.txt", b.res[0:2*51:2, 0:2*51:2], delimiter=" :: ")
np.savetxt("res3.txt", c.res[0:4*51:4, 0:4*51:4], delimiter=" :: ")

p_eff = eff_order(50, 50, a.res[1:51:1, 1:51:1], b.res[1:2*51:2, 1:2*51:2], c.res[1:4*51:4, 1:4*51:4])
np.savetxt("p_eff.txt", p_eff, delimiter=" & ")
