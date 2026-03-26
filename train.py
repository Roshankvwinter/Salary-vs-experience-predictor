import pandas as pd 
from sklearn.linear_model import LinearRegression 
import pickle 

# Load dataset 
df = pd.read_csv('salary_data.csv')

# Prepare data 
X = df[['YearsExperience']]
y = df['Salary']

# train model
model = LinearRegression()
model.fit(X, y)

# save model 
with open('model.pkl','wb') as f:
    pickle.dump(model, f)

print("Model training complete. Model saved as model.pkl")
print(f"coefficient: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}")