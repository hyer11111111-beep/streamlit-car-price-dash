# Streamlit Car Price Prediction App

This project is a Streamlit application designed to predict car purchasing amounts based on user input and perform exploratory data analysis on a car purchasing dataset. The application provides an interactive interface for users to explore the data and make predictions using a pre-trained machine learning model.

## Project Structure

```
streamlit-car-price-dash
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── pages
│   │   ├── home.py           # Home page with introduction and image
│   │   ├── eda.py            # Exploratory Data Analysis section
│   │   └── ml.py             # Machine Learning predictions section
│   ├── components
│   │   ├── ui.py             # Reusable UI components
│   │   └── charts.py         # Chart and visualization management
│   ├── styles
│   │   └── style.css         # Custom CSS styles for the app
│   ├── utils
│   │   ├── data_loader.py     # Functions for loading and processing data
│   │   └── preprocessing.py    # Functions for data preprocessing
│   └── assets
│       └── README.md         # Information about assets used in the project
├── data
│   └── Car_Purchasing_Data.csv # Dataset for analysis and predictions
├── model
│   └── regressor.pkl         # Pre-trained machine learning model
├── tests
│   ├── test_data.py          # Unit tests for data loading and preprocessing
│   └── test_models.py        # Unit tests for the machine learning model
├── requirements.txt          # List of dependencies for the project
├── .gitignore                # Files and directories to ignore by version control
└── README.md                 # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-car-price-dash
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```

Once the application is running, you can navigate through the different sections using the sidebar menu. The sections include:

- **Home**: An introduction to the application and its purpose.
- **EDA**: Explore the car purchasing dataset, view dataframes, basic statistics, and perform correlation analysis.
- **ML**: Input various features to predict car purchase amounts using the pre-trained model.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.