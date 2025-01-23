import pandas as pd
from sklearn.model_selection import train_test_split

vehicles = pd.read_csv("Raw_Datasets/vehicles.csv")

# Get the labels (response), dataframe (obs: it can also be a numpy array):
response = 'co2emissions'
y_vehicles = vehicles[[response]]
print(y_vehicles)

# Drop the column
X_vehicles = vehicles.drop(response, axis=1)
print(X_vehicles)

# It is also possible to select only the columns without the response
predictors = list(vehicles.columns)
predictors.remove(response)

X_vehicles_predictors = vehicles[predictors]
print(X_vehicles_predictors)

# Gets the same results:
print(type(X_vehicles), type(X_vehicles_predictors))
print(X_vehicles.shape, X_vehicles_predictors.shape)

# Split into test and training sets (default test_size = 0.25)
X_train, X_test, y_train, y_test = train_test_split(X_vehicles, y_vehicles)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# Split into test and training sets specifying test_size
X_train, X_test, y_train, y_test = train_test_split(X_vehicles, y_vehicles, test_size= 0.40)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# Split into test and training sets using stratify (keeping the proportions of the sets, on one column)
x_train, x_test, y_train, y_test = train_test_split(X_vehicles, y_vehicles, test_size = 0.01, stratify = X_vehicles['drive']) 