from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


titanic = pd.read_csv('Raw_Datasets/titanic.csv')
description = titanic.describe()
print(description)

# Treat null values:

nullSum = titanic.isnull().sum()
print(nullSum)

    # As age is independant for survival, null values can be replaced by the mean
    # OBS: Inplace changes the origin dataset.

titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)

    # Cabin has the most null values. But it can be seen that cabin has relation to survivability, so it cannot be just filled.
    # As survived is 0 or 1, the mean can be used to see the relation:

survivability_by_null_cabin = titanic.groupby(titanic['Cabin'].isnull())['Survived'].mean()
print(survivability_by_null_cabin) # Null values survive 30% of the time

    #  Create a cabin_indicator column to mark rows that have cabins, and rows that do not

titanic['Cabin_ind'] = np.where(titanic['Cabin'].isnull(), 0, 1)
print(titanic.head())

# Reduce columns number:

    # Drops not informational columns: (OBS: Now cabin can also be dropped with the new indicator)

titanic.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
print(titanic.head())

    # SibSp and Parch are fields related to the number of relatives in the dataframe, and graphs show that they have similar behavior (regard survivability)
    # Create a column to fuse those 2

titanic['Family_cnt'] = titanic['SibSp'] + titanic['Parch']

    # Drop the former columns (axis = 1)

titanic.drop(['PassengerId', 'SibSp', 'Parch'], axis=1, inplace=True)

# Label categorical values:

gender_num = {'male': 0, 'female': 1}

titanic['Sex'] = titanic['Sex'].map(gender_num)
print(titanic.head())

#Save as treated

titanic.to_csv('Treated_Datasets/titanic_treated.csv', index=False)

## Split data in training, evaluation and test; and save as CSV

    # Get features (X) and labels (y) datas

features = titanic.drop('Survived', axis=1)
labels = titanic['Survived']

    # Split in train and test (with 40% of the data on the test )

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.4, random_state=42)

    # Split test again, now to get test and validation groups. 

X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

for dataset in [y_train, y_val, y_test]:
    print(round(len(dataset) / len(labels), 2))

    # Save on many CSVs

X_train.to_csv('Treated_Datasets/Splited/titanic/train_features.csv', index=False)
X_val.to_csv('Treated_Datasets/Splited/titanic/val_features.csv', index=False)
X_test.to_csv('Treated_Datasets/Splited/titanic/test_features.csv', index=False)

y_train.to_csv('Treated_Datasets/Splited/titanic/train_labels.csv', index=False)
y_val.to_csv('Treated_Datasets/Splited/titanic/val_labels.csv', index=False)
y_test.to_csv('Treated_Datasets/Splited/titanic/test_labels.csv', index=False)



