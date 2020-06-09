# Create a CSV file with data for Poisson curve for 300 days.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# lambda = l
l = 180
poisson = lambda x : (l**x/math.factorial(x)) *(math.exp(l)) /3.2965239908584015e+151
x = list(range(300))
y = [round(poisson(i)) for i in x]

pd.DataFrame(y).T.to_csv('poisson.csv')