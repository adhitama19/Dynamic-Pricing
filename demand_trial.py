from __future__ import division, print_function

import os
import sys
import numpy as np
import scipy.optimize as optimize
import pandas as pd
import itertools

import matplotlib.pyplot as plt

def price(x, a=200, b=10, d=10, t=np.linspace(1,10,10)):

    """Returns the price given a demand x and time t"""

    return (a - b * x) * d / (d + t)

def demand(p, a=200, b=10, d=10, t=np.linspace(1, 10, 10)):
    """"Return demand given an array of prices p for times t"""

    return 1.0 / b * ( a - p * (d + t) / d)

# Lets explore the different demand curves

price_vals = np.array([5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 100.0, 200.0])
t_vals = np.array([1, 5, 10])
colors = ['red', 'blue', 'green']

for time, color in zip(t_vals, colors):
    plt.plot(price_vals, demand(price_vals, t=time), color=color, label='t = {}'.format(time))
plt.legend(loc=3)
plt.xlabel("price")
plt.ylabel("Demand")
plt.grid(False)
plt.show()

def objective(x_t, a=200, b=10, d=10, t=np.linspace(1,10,10)):
    return -1.0 * np.sum( x_t * price(x_t, a=a, b=b, d=d, t=t))

# Define constraint

def constraint_1(x_t, s_0=150):
    return s_0 - np.sum(x_t)

def constraint_2(x_t):
    return x_t

def constraint_3(x_t, a=200, b=10):
    return (a/b) - x_t

s_0 = 150
a = 200.0
b = 10.0
d = 10.0
t = np.linspace(1,10,10)

# Starting values:

x_start = 3.0 * np.ones(len(t))

# bounds on the values

bounds = tuple((0,20.0) for x in x_start)

constraints = ({'type': 'ineq', 'fun': lambda x, s_0=s_0: constraint_1(x, s_0=s_0)},
               {'type': 'ineq', 'fun': lambda x: constraint_2(x)},
               {'type': 'ineq', 'fun': lambda x, a=a, b=b: constraint_3(x, a=a, b=b)})

opt_results = optimize.minimize(objective, x_start, args=(a, b, d, t),
                                method='SLSQP', bounds=bounds, constraints=constraints)

# print(opt_results)
#
# print(np.sum(opt_results['x']))

print(np.linspace(1, 10, 10))


#     # Set price historical and demand historical
#     demand_level = None
#     np_demand_level = np.zeros(shape=(time,))
#
#     # Creating numpy array for demand_level
#     for i in range(time):
#
#         if demand_level is None:
#             demand_level = round(np.random.uniform(50, 150), 1)
#             np_demand_level[i] = demand_level
#
#         else:
#             demand_level = np.random.poisson(demand_level)
#             np_demand_level[i] = demand_level
#
#     return np_demand_level
#
# arrival_Rate = np.random.uniform(50, 150)
# sample_From_Arrival = np.random.sample(arrival_Rate)
#
# print(sample_From_Arrival)

# def linear_demand(p, m, d):
#
#     return m * p + d
#
# d_Array = create_Demand(1,10)
#
#
#
# for i in range(1,101):
#     print(linear_demand(price[i], -1, i))
#
#
# plt.plot(price, demand)
# plt.title("Price-response Function")
# plt.xlabel("Price")
# plt.ylabel("Demand")
# plt.show()