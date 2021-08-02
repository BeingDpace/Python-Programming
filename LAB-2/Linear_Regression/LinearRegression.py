
import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
from sklearn import datasets

# load diabetes datasets using sklearn
diabetes = datasets.load_diabetes() 
X, y = datasets.load_diabetes(return_X_y=True)
# Use only one feature
X = X[:, np.newaxis, 2]
# feature matrix shape
print(diabetes.data.shape)
# X shape
print(X.shape)
# target vector shape 
print(y.shape) 

# Splitting train and test datasets in 70%-30% ratio
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#Using Linear regression model from sklearn
model = LinearRegression()
# fitting the train datasets in the model
model.fit(X_train, y_train)
#predicting the test dataset
y_pred = model.predict(X_test)
#print("Mean squared error: ", mean_squared_error(y_test, y_pred))

#Plotting output
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
