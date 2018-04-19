from numpy import *
from scipy.integrate import *
from scipy.optimize import *

def main():
	# print(quad(lambda x:exp(-x),0,inf))
	# print(dblquad(lambda t,x:exp(-x*t)/t**3, 0, inf, lambda x:1, lambda x:inf))
	# def f(x,y):
	# 	return x*y
	# def bound_y():
	# 	return [0,0.5]
	# def bound_x(y):
	# 	return [0,1-2*y]
	# print(nquad(f, [bound_x, bound_y]))
	def rosen(x):
		return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
	x0 = array([1.3,0.8,0.7,1.9,1.2])
	res =  minimize(rosen,x0,method='nelder-mead', options={'xtol':1e-8, 'disp':True})
	print('ROSE MINI:', res.x)
	def func_deriv(x):
		dfdx0 = (-2*x[0]-2*x[1]+2)
		dedx1 = (2*x[0]-4*x[1])
		return array([dfdx0, dfdx1])
	cons = ({})


if __name__ == '__main__':
	main()