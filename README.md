
# Heart Disease Prediction

## 🩺 Overview

This project aims to predict the likelihood of heart disease in patients based on various medical attributes such as age, sex, blood pressure, cholesterol levels, and other health indicators. By leveraging machine learning algorithms, the model assists in early detection, potentially guiding preventive measures and treatment plans.

## 🔧 Technologies Used

- **Programming Language:** Python
- **Libraries & Frameworks:**
  - `Flask` – for building the web application
  - `scikit-learn` – for machine learning algorithms
  - `pandas` – for data manipulation
  - `numpy` – for numerical operations
  - `matplotlib` & `seaborn` – for data visualization
- **Model:** Random Forest Classifier

## 📊 Dataset

The dataset used in this project is sourced from the [UCI Heart Disease Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). It contains 303 instances with 14 attributes, including:

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Serum cholesterol
- Fasting blood sugar
- Resting electrocardiographic results
- Maximum heart rate achieved
- Exercise induced angina
- Oldpeak depression induced by exercise relative to rest
- Slope of the peak exercise ST segment
- Number of major vessels colored by fluoroscopy
- Thalassemia

## ⚙️ Features

- **User Authentication:** Secure login and registration system.
- **Prediction Interface:** Input personal health data to receive heart disease risk assessment.
- **Model Training:** Utilizes a Random Forest Classifier for prediction.
- **Web Interface:** Developed using Flask for user interaction.

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Meghana-2124/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies

Ensure you have Python 3.6+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the Flask development server:

```bash
python main_app.py
```

Access the application by navigating to `http://127.0.0.1:5000/` in your web browser.

## 📈 Model Training

The machine learning model is trained using the Random Forest Classifier. The training process involves:

- **Data Preprocessing:** Handling missing values, encoding categorical variables, and scaling numerical features.
- **Model Training:** Splitting the dataset into training and testing sets, followed by training the model.
- **Evaluation:** Assessing model performance using metrics like accuracy, precision, recall, and F1-score.

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
