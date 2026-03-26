import numpy as np 
import pandas as pd 

# Generate synthetic data 
np.random.seed(42)
years_exp = np.random.uniform(0, 10, 100)
salary = 20000 + 5000 * years_exp + np.random.normal(0,10000,100)

# create dataframe and save to csv 
df = pd.DataFrame({'YearsExperience': years_exp, 'Salary': salary})
df.to_csv('salary_data.csv', index = False)
print("Dataset generated and saved as salalry_data.csv")
