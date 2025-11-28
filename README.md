# ML Project - Student Performance Prediction

A machine learning project for predicting student performance based on various demographic and socioeconomic factors. This project includes data ingestion, exploratory data analysis (EDA), model training, and a Flask web application for predictions.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Technologies Used](#technologies-used)

## 🎯 Project Overview

This machine learning project aims to predict student performance (likely math scores) based on:
- **Demographics**: Gender, race/ethnicity
- **Socioeconomic Factors**: Parental education level, lunch type
- **Academic Preparation**: Test preparation course completion
- **Academic Performance**: Reading and writing scores

The project implements multiple regression models and selects the best-performing one using hyperparameter tuning and cross-validation.

## ✨ Features

- **Data Pipeline**: Automated data ingestion and transformation
- **Model Comparison**: Tests 7+ different regression algorithms:
  - Random Forest
  - Decision Tree
  - Gradient Boosting
  - Linear Regression
  - XGBoost
  - CatBoost
  - AdaBoost
- **Hyperparameter Tuning**: Grid search for optimal model parameters
- **Flask Web App**: Interactive web interface for making predictions
- **Custom Exception Handling**: Robust error management
- **Logging System**: Comprehensive logging for debugging and monitoring
- **Model Persistence**: Serialized models for quick inference

## 📁 Project Structure

```
Mlproject/
├── artifacts/                    # Generated data and model artifacts
│   ├── raw.csv                   # Raw input data
│   ├── train.csv                 # Training dataset
│   ├── test.csv                  # Test dataset
│   └── model.pkl                 # Trained model
├── catboost_info/                # CatBoost training metrics
├── logs/                         # Application logs
├── notebook/                     # Jupyter notebooks
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv
├── src/                          # Main source code
│   ├── __init__.py
│   ├── exception.py              # Custom exception handling
│   ├── logger.py                 # Logging configuration
│   ├── utils.py                  # Utility functions
│   ├── components/               # Core ML components
│   │   ├── data_ingestion.py     # Load and split data
│   │   ├── data_transformation.py # Feature preprocessing
│   │   └── model_trainer.py      # Model training and selection
│   └── pipeline/                 # Prediction & training pipelines
│       ├── predict_pipeline.py   # Inference pipeline
│       └── train_pipeline.py     # Training workflow
├── templates/                    # HTML templates for Flask
│   ├── index.html                # Home page
│   └── home.html                 # Prediction form
├── app.py                        # Flask application entry point
├── setup.py                      # Project setup configuration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mlproject
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the project in development mode**
   ```bash
   pip install -e .
   ```

## 🚀 Usage

### Running the Web Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

**Usage Steps:**
1. Visit the home page at `http://localhost:5000`
2. Click on the prediction form link
3. Fill in the student information:
   - Gender
   - Race/Ethnicity
   - Parental Level of Education
   - Lunch Type
   - Test Preparation Course (completed/none)
   - Reading Score
   - Writing Score
4. Submit to get the predicted score

### Running the Training Pipeline

To train a new model:
```bash
python -c "from src.pipeline.train_pipeline import TrainPipeline; pipeline = TrainPipeline(); pipeline.initiate_training()"
```

Or use the notebooks:
- **1. EDA STUDENT PERFORMANCE.ipynb** - Exploratory data analysis
- **2. MODEL TRAINING.ipynb** - Model training workflow

## 🤖 Model Training

### Data Pipeline

1. **Data Ingestion** (`data_ingestion.py`):
   - Loads raw data from CSV
   - Splits into training (80%) and test (20%) sets

2. **Data Transformation** (`data_transformation.py`):
   - Handles categorical encoding (gender, ethnicity, education level, etc.)
   - Applies feature scaling using StandardScaler
   - Handles missing values

3. **Model Training** (`model_trainer.py`):
   - Trains multiple regression models
   - Performs hyperparameter tuning with GridSearchCV
   - Evaluates models using R² score and other metrics
   - Saves the best-performing model

### Model Selection

The system evaluates the following models:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The model with the highest R² score on the test set is selected and saved.

## 🌐 Web Application

The Flask application provides:
- **Home Page** (`/`): Landing page with navigation
- **Prediction Endpoint** (`/predict`):
  - GET: Displays the prediction form
  - POST: Processes form data and returns prediction

### API Usage

```python
# Custom data preparation
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create custom data
data = CustomData(
    gender='male',
    race_ethnicity='group B',
    parental_level_of_education='some high school',
    lunch='standard',
    test_preparation_course='completed',
    reading_score=72,
    writing_score=74
)

# Get prediction
pred_df = data.get_data_as_data_frame()
predict_pipeline = PredictPipeline()
result = predict_pipeline.predict(pred_df)
print(f"Predicted Score: {result[0]}")
```

## 📦 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computations |
| **scikit-learn** | Machine learning algorithms and preprocessing |
| **XGBoost** | Gradient boosting models |
| **CatBoost** | Categorical boosting |
| **Flask** | Web application framework |
| **matplotlib & seaborn** | Data visualization |
| **dill** | Model serialization |

## 📊 Dataset

The project uses a student performance dataset with the following features:

- **Gender**: male/female
- **Race/Ethnicity**: group A-E
- **Parental Level of Education**: high school, some college, bachelor's, master's, associate's
- **Lunch**: standard/free/reduced
- **Test Preparation Course**: completed/none
- **Reading Score**: 0-100
- **Writing Score**: 0-100
- ****Target**: Math Score (0-100)

## 📈 Model Performance

Models are evaluated using:
- **R² Score**: Coefficient of determination
- **Mean Squared Error (MSE)**
- **Cross-validation scores**

## 🔍 Logging and Error Handling

- Custom exception handling with detailed error messages
- Comprehensive logging to track model training and predictions
- Logs stored in `logs/` directory for debugging

## 📝 License

This project is part of an educational machine learning course.

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact & Support

For questions or issues, please open an issue on the repository.

---

**Last Updated**: November 2025
