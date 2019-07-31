# Import necessary library and package
import demand
import competitor_A as a
import competitor_B as b
import competitor_C as c
import random
import numpy as np
import matplotlib.pyplot as plt

# Assign the number of competitor and time periods
num_of_competitor = 3
t = 10
s = 5

# Create demand
demand_Array = demand.create_Demand(s,t)

# ==================== Price =======================

# Initialize price array and revenue array
arr_price = np.zeros(shape=(t, num_of_competitor))
arr_min_price = np.zeros(shape=(t, num_of_competitor))

# Simulation for loop

for time in range(t):

    # Set price for each competitor
    arr_price[time, 0] = a.create_randomInt(10, 20) #A
    arr_price[time, 1] = b.create_randomInt(10, 20) #B
    arr_price[time, 2] = c.create_randomInt(10, 20) #C

    # Get the minimum price and its index in each row
    min_Price = np.amin(arr_price[time])
    print("Minimum Price: ", min_Price)
    print("Willingness to Pay ", demand_Array[time, 1])
    min_Index = np.where(arr_price[time] == min_Price)
    same_Price = np.amax(min_Index) + 1

    # Check if there are any same price
    if demand_Array[time, 1] >= min_Price:

        if same_Price > 1:
            # Set the revenue for each competitor split the demand
            arr_min_price[time, min_Index] = round(min_Price * (demand_Array[time, 0]/same_Price),1)

        else:
            # Set the revenue for competitor with lowest price
            arr_min_price[time, min_Index] = round(min_Price * demand_Array[time, 0], 1)

    else:

        None


print("Price array:\n", arr_price)
print("Revenue array:\n", arr_min_price)

# Print the profit for each competitor
profit = np.sum(arr_min_price, axis=0)
print("The profit: ", profit)



