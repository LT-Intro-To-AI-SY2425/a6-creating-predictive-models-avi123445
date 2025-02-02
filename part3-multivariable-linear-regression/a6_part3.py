import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles", "age"]].values
y = data["Price"].values


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.2)


model = LinearRegression().fit(xtrain, ytrain)

coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

print(f"Model's Linear Equation: y = {coef[0]}x1 + {coef[1]}x2 + {intercept}")
print("R Squared value:", r_squared)

predict = model.predict(xtest)
predict = np.around(predict, 2)
print("Predicted prices:", predict)

# Use a 2D array as input for model.predict
# specific_input = np.array([[150000, 50]])
# predict = model.predict(specific_input)
# predict = np.around(predict, 2)

print("Predicted price for 10 miles and 89,000 years old car:", predict)


x_1 = x[:, 0]  
x_2 = x[:, 1]  

fig, graph = plt.subplots(2, 1, figsize=(8, 6))

graph[0].scatter(x_1, y, color='blue')
graph[0].set_xlabel("Total Miles")
graph[0].set_ylabel("Price")

y_fit_1 = coef[0] * x_1 + intercept
graph[0].plot(x_1, y_fit_1, color='red', label='Best Fit Line (Miles vs Price)')
graph[0].legend()

graph[1].scatter(x_2, y, color='green')
graph[1].set_ylabel("Price")
graph[1].set_xlabel("Car Age")

y_fit_2 = coef[1] * x_2 + intercept
graph[1].plot(x_2, y_fit_2, color='red', label='Best Fit Line (Age vs Price)')
graph[1].legend()

corr_miles = np.corrcoef(x_1, y)[0, 1]
corr_age = np.corrcoef(x_2, y)[0, 1]

print(f"Correlation between Total Miles and Car Price: {round(corr_miles, 3)}")
print(f"Correlation between Age and Car Price: {round(corr_age, 3)}")

plt.tight_layout()
plt.show()
