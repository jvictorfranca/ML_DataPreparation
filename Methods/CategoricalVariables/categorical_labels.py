import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

census = pd.read_csv('Raw_Datasets\census.csv')
print(census)

# Label encoder  to encode categorical strings

    # Create a specific Label encoder for each column
label_encoder_workclass = LabelEncoder()
label_encoder_workclass_np = LabelEncoder()

    # Use to encode column
encoded_workclass = label_encoder_workclass.fit_transform(census['workclass'])
print(encoded_workclass)

    # Replace column with encoded:
census['workclass'] = encoded_workclass
print(census)

    # Can also be used to form on a numpy array:
encoded_workclass_np = label_encoder_workclass.fit_transform(census['workclass'].values)
print(encoded_workclass_np)


# Label encoder to decode categorical strings:

    # Use decode method:
decoded_workclass = label_encoder_workclass.inverse_transform(encoded_workclass)
print(decoded_workclass)

# Label stratification with OneHotEncoder (after label encoder)
    # Need to pass the column index of OneHotEncoder, the 'workclass' index is 1. It could receive more columns on the list. 
    # OBS: The passthrough means that one hot encoder wont delete the "workclass" column
onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
census_hot_encoded_array = onehotencoder_census.fit_transform(census)
print(census_hot_encoded_array)
    #OBS: You can pass the NP array as X to train on Scikit-learn.

    # You can get the name of the params on the oneHotEncoder
one_hot_columns = onehotencoder_census.get_feature_names_out()
print(one_hot_columns)

    #  You can create a dataframe again
census_hot_encoded = pd.DataFrame(census_hot_encoded_array, columns=one_hot_columns)
print(census_hot_encoded)


