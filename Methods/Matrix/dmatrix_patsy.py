
import seaborn as sns

import patsy

titanic = sns.load_dataset('titanic')

titanic.head()


# Transforms the notation in a design matrix 
y, X = patsy.dmatrices('survived ~ pclass + sex + age + sibsp + parch + fare + embarked', data=titanic, return_type="dataframe")

print(X.head())