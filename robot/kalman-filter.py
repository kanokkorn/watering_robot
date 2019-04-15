#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np 

measurements = [5, 6, 7, 9, 10,]
motions = [1, 1, 2, 1, 1]
measurements_sig = 4
motion_sig = 2
mu = 0
sig = 100000 


def f(mu, sigma, x):
    coefficient = 1.0 / math.sqrt(2.0*math.pi*sigma)
    exponential = math.exp(-0.5*(x-mu)**2/sigma)
    return coefficient*exponential

def update(mean1, var1, mean2, var2):
    new_mean = (var2*mean1+var1*mean2)/(var2+var1)
    new_var = 1/(1/var2+1/var1)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1+ mean2
    new_var = var1 + var2
    return [new_mean, new_var]

for n in range(len(measurements)):
    mu, sig = update(mu, sig, measurements[n], measurements_sig)
    print('Update: [{}, {}]'.format(mu, sig))
    mu, sig = predict(mu, sig, motions[n], motion_sig)
    print('Predict: [{}, {}]'.format(mu, sig))

print('\n')
print('Final result: [{}, {}]'.format(mu, sig))

mu = mu
sigma2 = sig

x_axis = np.arange(-20, 20, 0.1)

g = []
for x in x_axis:
    g.append(f(mu, sigma2, x))
plt.plot(x_axis, g)
plt.show()