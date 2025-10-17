Crop Prediction Model using Machine Learning

A user-friendly web application built with Flask and Python that recommends the most suitable crop to grow based on soil and environmental conditions. This project aims to empower farmers with data-driven insights to maximize their agricultural yield and profitability.

🌾 The Problem it Solves

In many agricultural regions, including areas like Macherla, Andhra Pradesh, farmers traditionally rely on experience and intuition passed down through generations to decide which crops to plant. However, this approach can be unreliable due to:

Changing Climate: Unpredictable weather patterns and fluctuating temperatures make traditional knowledge less effective.

Soil Degradation: Over time, the nutrient profile of the soil changes, and what worked in the past may no longer be optimal.

Lack of Information: Farmers often lack access to scientific data about which crop would be most productive for their specific soil composition and local climate.

This uncertainty can lead to lower yields, financial losses, and inefficient use of resources like water and fertilizers. Our Crop Prediction Model directly addresses this challenge by providing a fast, accessible, and scientific recommendation, helping farmers make informed decisions to secure their livelihood.

✨ Features

Intuitive Prediction Form: A simple and clean UI where users can input soil and environmental parameters.

Instant Crop Recommendation: Utilizes a pre-trained machine learning model to provide an immediate prediction for the most suitable crop.

Accessible Dataset Viewer: An integrated feature that allows users to view the complete dataset used to train the model, promoting transparency and providing valuable data for reference.

Responsive Design: The interface is designed to be accessible on both desktop and mobile devices.

📊 About the Dataset

The model was trained on the Crop_recommendation.csv dataset, which contains 2200 data points. It includes the following key environmental and soil-related features:

N: Ratio of Nitrogen content in the soil.

P: Ratio of Phosphorus content in the soil.

K: Ratio of Potassium content in the soil.

Temperature: Temperature in degrees Celsius.

Humidity: Relative humidity in %.

pH: pH value of the soil.

Rainfall: Rainfall in mm.

Label: The target variable, representing one of 22 different crop types (e.g., Rice, Maize, Chickpea, Coffee, etc.).

💻 Technology Stack

This project is built using a combination of backend, frontend, and machine learning technologies:

Backend

Python: The core programming language for the application logic and machine learning.

Flask: A lightweight micro web framework used to build the web server and handle requests.

Pandas & NumPy: Used for data manipulation, loading the dataset, and numerical operations.

Frontend

HTML5: For the structure and content of the web pages.

CSS3: For styling the user interface, including the responsive layout and custom fonts.

Bootstrap (on Dataset page): Used for quickly styling the data table to be clean and readable.

Machine Learning

Scikit-learn: For building and training the prediction model.

Pickle: Used for serializing the trained machine learning model into a file (.pkl) so it can be loaded and used for predictions in the Flask app.

📂 Project Structure

├── crop-prediction-flask-app/
│
├── crop_trained_model.pkl      # Serialized trained machine learning model
├── Crop_recommendation.csv     # The dataset file
├── app.py                      # Main Flask application script
├── model.py                    # (Optional) Script for training the model
├── .gitignore                  # Specifies files for Git to ignore
├── README.md                   # This README file
│
├── static/
│   └── farm.jpg                # Background image
│
└── templates/
    ├── index.html              # Main prediction page
    └── dataset.html            # Dataset viewer page


🚀 Setup and Installation

To run this project on your local machine, follow these steps:

Clone the Repository

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/thorlikondasivaprasad/Crop-Prediction-Flask-App.git)
cd your-repo-name


Create a Virtual Environment
It's recommended to create a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


Install Dependencies
You will need to create a requirements.txt file containing the necessary libraries.
requirements.txt:

Flask
numpy
pandas
scikit-learn


Then, install them using pip:

pip install -r requirements.txt


Run the Flask App

python app.py


Open in Browser
Navigate to http://127.0.0.1:5000 in your web browser to see the application live.
