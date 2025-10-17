#Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv('Crop_recommendation.csv')  # Replace 'crop_data.csv' with your dataset file

# Split the data into features and labels
x = data.iloc[:,:-1] #Features - all rows data with except 1 label column 
y = data.iloc[:,-1]  #Labels - all rows data with only Label column

# Split the data into training and testing sets
x_train,xtest, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)

# Create the model
model = RandomForestClassifier()

# Train the model -> x_train,y_train are required to train the model
model.fit(x_train, y_train)

# Make predictions on test data 
# we use only (x_test) -> this is the data row sample, model can be tested
# predictions = model.predict(X_test)

# Pickling saves trained models to disk, allowing them to be
# reused for predictions "without retraining", which is more efficient and necessary for "deployment".

# Open a file in binary write mode ("wb").
with open('crop_trained_model.pkl', 'wb') as file:
    # Use pickle.dump() to write the model object to the file.
    pickle.dump(model , file)


# Evaluate the model
# accuracy = model.score(X_test, y_test)
# print("Accuracy:", accuracy)

# Example usage: Predict crop for a new set of features
# new_features = [[]]  # Replace with your own set of features
# predicted_crop = model.predict(new_features)
# print("Predicted crop:", predicted_crop)
