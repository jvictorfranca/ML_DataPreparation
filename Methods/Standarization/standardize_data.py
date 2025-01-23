# Use z-score Normalization:

import pandas as pd
from sklearn.preprocessing import StandardScaler
vehicles = pd.read_csv("Raw_Datasets/vehicles.csv")

# Use standardScaler to normalize a column emission (in a numpyArray):
np_co2emissions_zm = StandardScaler().fit_transform(vehicles[['co2emissions']])
print(np_co2emissions_zm)

# Return to a pandas dataframe column:
pd_co2emissions_zm = pd.DataFrame(np_co2emissions_zm, columns = ['co2emissions_standardized'])
print(pd_co2emissions_zm)