import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import pickle
from flask import Flask, request, jsonify

# Load the dataset
data = pd.read_csv('vgsales.csv')

# Preprocess the data
# Handle missing values (if any)
data = data.dropna()

# Encode categorical variables
categorical_cols = ['Platform', 'Genre', 'Publisher']
numerical_cols = ['Rank', 'Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# Create column transformer
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
preprocessor = ColumnTransformer(transformers=[('encoder', categorical_transformer, categorical_cols)],
                                 remainder='passthrough')

# Transform data
X = preprocessor.fit_transform(data[categorical_cols + numerical_cols])
y = data['Global_Sales']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Flask app
app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Preprocess the input data
    input_data = pd.DataFrame(data, index=[0])
    categorical_cols = ['Platform', 'Genre', 'Publisher']
    numerical_cols = ['Rank', 'Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    preprocessed_data = preprocessor.transform(input_data[categorical_cols + numerical_cols])

    # Make predictions using the loaded model
    prediction = model.predict(preprocessed_data)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
