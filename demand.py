import random
import matplotlib.pyplot as plt
import numpy as np

price = list(range(0,101))
demand = list(range(0, 101))

empty_Linear = []

def create_Demand(simul,time):
    """This will create random demand"""

    np_demand_level = np.zeros(shape=(time,2))


    for s in range(simul):

        arrival_Rate = np.random.uniform(50, 150)

        for t in range(time):
            arrivals = np.random.poisson(arrival_Rate)

            # Now i need to find out how to model the willingness to pay
            wtp = round(np.random.uniform(1,30), 1)
            np_demand_level[t, 0] = arrivals
            np_demand_level[t, 1] = wtp

    return(np_demand_level)


# Linear price-response function
def linear(p, m, d):

    return m * p + d

dem = list(range(0,101))
pri = list(range(0,101))

for i in range(1,102):
    res = linear(pri[i - 1], -1, dem[-i])
    empty_Linear.append(res)

print(empty_Linear)

# Plot the linear price-response function
plt.plot(pri, empty_Linear, '--bo')
plt.xlabel("Price")
plt.ylabel("Demand")
plt.show()














