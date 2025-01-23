import pandas as pd
from sklearn.preprocessing import MinMaxScaler

vehicles = pd.read_csv("Raw_Datasets/vehicles.csv")

# Use minMax to normalize a column emission (in a numpyArray):
np_co2emissions_mm = MinMaxScaler().fit_transform(vehicles[['co2emissions']])
print(np_co2emissions_mm)

# Return to a pandas dataframe column:
pd_co2emissions_mm = pd.DataFrame(np_co2emissions_mm, columns = ['co2emissions_normalized'])
print(pd_co2emissions_mm)