import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

coffee = pd.read_csv('/Users/cristosaidsalaslandaverde/Documents/machine-learning/data-transformations/starbucks_customers.csv')
ages = coffee['age']
mean_age = np.mean(ages)
std_dev_age = np.std(ages)
ages_standarized = (ages - mean_age) / std_dev_age
print(ages_standarized)