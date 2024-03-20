# Video Game Sales Prediction

This project aims to train a machine learning model to predict the global sales of video games based on various features such as platform, genre, publisher, and sales in different regions.

## Dataset

The dataset used in this project is the "Video Game Sales" dataset from Kaggle, which contains information about video games with sales greater than 100,000 copies. The dataset includes features such as:

- Rank
- Name
- Platform
- Year
- Genre
- Publisher
- Sales in North America (NA_Sales)
- Sales in Europe (EU_Sales)
- Sales in Japan (JP_Sales)
- Sales in other regions (Other_Sales)
- Global Sales

## Project Structure

The project has the following structure:

```
video-game-sales-prediction/
├── data/
│   └── vgsales.csv
├── Dockerfile
├── Makefile
├── main.py
├── model.pkl
├── README.md
└── requirements.txt
```

- `data/`: Directory to store the dataset.
- `Dockerfile`: Docker configuration file to build the application container.
- `Makefile`: Makefile with commands for installing dependencies, running the Flask app, building the Docker image, and running the container.
- `main.py`: Python script containing the code for data preprocessing, model training, and Flask API.
- `model.pkl`: Trained machine learning model saved as a pickle file.
- `README.md`: This file, containing project documentation.
- `requirements.txt`: List of Python dependencies required by the project.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/your-username/video-game-sales-prediction.git
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Download the "Video Game Sales" dataset from Kaggle and place the `vgsales.csv` file in the `data/` directory.

## Usage

### Local Development

To run the Flask app locally, use the following command:

```
make dev
```

This will clean up any cached files, install dependencies, and start the Flask server.

### Docker

To build the Docker image and run the container, use the following command:

```
make prod
```

This will clean up any cached files, install dependencies, build the Docker image, and run the container.

The Flask app will be accessible at `http://localhost:5000/predict`.

### API Endpoint

The `/predict` endpoint accepts POST requests with a JSON payload containing the input data for prediction. The input data should have the following format:

```json
{
    "Rank": 1,
    "Platform": "PS4",
    "Year": 2018,
    "Genre": "Action",
    "Publisher": "Sony Computer Entertainment",
    "NA_Sales": 10.0,
    "EU_Sales": 5.0,
    "JP_Sales": 2.0,
    "Other_Sales": 3.0
}
```

The endpoint will return a JSON response with the predicted global sales for the given input data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

This README.md file provides an overview of the project, including the dataset used, project structure, setup instructions, usage guidelines for local development and Docker, information about the API endpoint, and instructions for contributing to the project.

Feel free to modify the content according to your specific project details, such as the repository URL, contribution guidelines, and license information.