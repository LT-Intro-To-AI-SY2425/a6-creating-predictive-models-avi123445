import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)

# Create the model
model = LinearRegression().fit(xtrain, ytrain)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)

# Print out the linear equation and r squared value:
print("Model's Linear Equation: y=",coef, "x +", intercept)
print("R Squared value:", r_squared)
'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
xtest=xtest.reshape(-1,1)
# get the predicted y values for the xtest values - returns an array of the results
predi = model.predict(xtest)
# round the value in the np array to 2 decimal places
predi = np.around(predi, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predi[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print("x value:", float(x_coord[0]), "Predicted y value:", predicted_y, "Actual y value:", actual)


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(8,6))
plt.scatter(xtrain,ytrain, c="black", label="Training Data")
plt.scatter(xtest, ytest, c="orange", label="Testing Data")
plt.scatter(xtest, predi, c="yellow", label="Predictions")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure By Age")
plt.plot(x, coef*x + intercept, c="b", label="Line of Best Fit")
plt.legend()
plt.show()
