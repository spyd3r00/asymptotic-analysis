from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import math

nth = int(input(" Enter a number: "))
timerList = []
result = []

###############################################

def constant():
	print("constant")
	start = timer()
	print("result: ",1)
	result.append(1)
	end = timer()

	constantTimer = end - start
	print ("exeution time: ",constantTimer)
	timerList.append(constantTimer)
constant()

###############################################

def logarithmic(nth):
	print("\nLogarithmic")
	start = timer()
	loga = (math.log(nth))
	result.append(loga)
	print("result: ",loga)
	end = timer()
	logTimer = end - start
	print ("execution time: ",logTimer)
	timerList.append(logTimer)
logarithmic(nth)

###############################################

def linearithmic(nth):
	print("\nLinearithmic")
	start = timer()
	line = (nth*math.log(nth))
	result.append(line)
	print ("Result: ",line)
	end = timer()

	linearithTimer = end - start
	print ("execution time: ",linearithTimer)
	timerList.append(linearithTimer)
linearithmic(nth)

###############################################

def linear(nth):
	print("\nLinear")
	start = timer()
	print("result: ",nth)
	result.append(nth)
	end = timer()
	lineTimer = end - start
	print ("execution time: ",lineTimer)
	timerList.append(lineTimer)
linear(nth)

###############################################

def quadratic(nth):
	print("\nQuadratic")
	start = timer()
	quad = nth**2
	result.append(quad)
	print("result: ",quad)
	end = timer()
	quadTimer = end - start
	print ("execution time: ",quadTimer)
	timerList.append(quadTimer)
quadratic(nth)

##############################################

def polynomial(nth):
	print("\nPolynomial")
	start = timer()
	poly = nth**3
	result.append(poly)
	print("result: ",poly)
	end = timer()
	polyTimer = end - start
	print ("execution time: ",polyTimer)
	timerList.append(polyTimer)
polynomial(nth)

############################################

def exponential(nth):
	print("\nExponential")
	start = timer()
	expo = 2**nth
	result.append(expo)
	print("result: ",expo)
	end = timer()
	expoTimer = end - start
	print ("execution time: ",expoTimer)
	timerList.append(expoTimer)
exponential(nth)

############################################

name = ['constant','logarithmic','linearithmic','Linear','quadratic','polynomial','exponential']
xResult = [result[0],result[1],result[2],result[3],
		result[4],result[5],result[6]]



plt.figure(figsize=(10, 5))


plt.subplot(2,1,1)
plt.plot(name, xResult)
plt.suptitle('Execution Time & Result')
plt.show()