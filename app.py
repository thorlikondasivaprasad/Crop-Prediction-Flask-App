import numpy as np
import pandas as pd # Import pandas to handle the dataset
from flask import Flask, request, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("crop_trained_model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    # The prediction is often an array, so we take the first element
    crop_name = prediction[0]
    return render_template("index.html", prediction_text = f"The Predicted Crop is {crop_name}")

@flask_app.route("/dataset")
def dataset():
    # Read the CSV file into a pandas DataFrame
    # Make sure 'Crop_recommendation.csv' is in your project's root folder
    try:
        df = pd.read_csv("Crop_recommendation.csv")
        # Convert the DataFrame to an HTML table, adding some bootstrap classes for styling
        table_html = df.to_html(classes='table table-striped table-hover', index=False, justify='center')
        return render_template("dataset.html", table=table_html)
    except FileNotFoundError:
        return "Error: Dataset file 'Crop_recommendation.csv' not found. Please add it to the project directory."


if __name__ == "__main__":
    flask_app.run(debug=True)
