import pandas as pd
import numpy as np

base_credit = pd.read_csv('Raw_Datasets\credit_data.csv')
print(base_credit)

# Clean negative values (that are impossible to be negative)
    # Filter wrong values
filtered_age_base_credit_loc = base_credit.loc[base_credit['age'] < 0]
filtered_age_base_credit = base_credit[base_credit['age'] < 0]
print(filtered_age_base_credit_loc, filtered_age_base_credit)
print(type(filtered_age_base_credit_loc),type(filtered_age_base_credit))

    # Get value indexes
base_credit_negative_age_indexes = filtered_age_base_credit.index
    
    # Drop those indexes, check if there are not negative values on the resulting DF.
base_credits_cleared_age = base_credit.drop(base_credit_negative_age_indexes)
print(base_credits_cleared_age[base_credits_cleared_age['age'] < 0])


# Replace negative values (that are impossible to be negative) with mean
    # Get mean of the valid values 
base_credits_mean_age = base_credit['age'][base_credit['age'] > 0].mean()
    # Replace invalid values with mean
filtered_base_credit = base_credit
filtered_base_credit[base_credit['age'] < 0] = base_credits_mean_age
print(filtered_base_credit[base_credit['age'] < 0])
