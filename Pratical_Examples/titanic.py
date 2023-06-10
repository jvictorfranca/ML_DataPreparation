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



