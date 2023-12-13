import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values
print(data)

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")
print(f"Model's Linear Equation: y={coef[1]}x2+ {intercept}")
print("R Squared value:", r_squared)
'''
X = x.reshape(-1, 1)
predict = model.predict(10000)
predict = np.around(predict, 2)
print(predict)'''

xtest = list(xtest)
xtest.append([89000, 10])
xtest.append([150000, 20])

ytest = list(ytest)
ytest.append(89000)
ytest.append(150000)


predict = model.predict(xtest)
preidct = np.around(predict, 2)
print(predict)

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print(f"Miles: {x_coord[0]} Age: {x_coord[1]} Actual: {actual} Predicted: {predicted_y}")