
# 🏥 Medical Insurance Charges Prediction

This project builds and deploys a machine learning model to predict **medical insurance charges** based on user inputs such as age, BMI, smoking status, etc. It includes exploratory analysis, model training, and a Streamlit web app for predictions.

---

## 📁 Project Structure

```
📦 Medical Insurance Charges/
├── app.py                    # Streamlit app for prediction UI
├── Medical_Insurance.ipynb   # Jupyter notebook with EDA, feature engineering, and modeling
├── one.pkl                   # Saved OneHotEncoder for categorical data
├── rf_model.pkl              # Trained Random Forest Regressor model
├── README.md                 # Project documentation
```

---

## 📊 Dataset Description

The dataset contains:

| Feature   | Description                            |
|-----------|----------------------------------------|
| age       | Age of the individual                  |
| sex       | Gender                                 |
| bmi       | Body Mass Index                        |
| children  | Number of children                     |
| smoker    | Smoking status                         |
| region    | Residential region in the US           |
| charges   | Target variable (insurance charges)    |

---

## 🔍 Key Features

- Exploratory Data Analysis (EDA)
- One-hot encoding for categorical features
- Correlation heatmap with `charges`
- Log transformation for skewed data
- Feature importance using Random Forest
- Model comparison: Linear Regression vs Random Forest
- Model evaluation with R² Score & MSE
- Model and encoder saved using `.pkl` format
- Interactive prediction using Streamlit

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/AkramGamal1/medical-insurance-prediction.git
cd medical-insurance-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

---

## 🧪 Sample Input

| Age | Sex   | BMI  | Children | Smoker | Region     |
|-----|-------|------|----------|--------|------------|
| 35  | Male  | 27.5 | 2        | Yes    | southeast  |

---

## ✅ Output

The app returns the predicted insurance charges based on the input.

---

## 📸 Preview

![input-image]("D:\DEPI\Medical Insurance Charges\input.png")
![output-image]("D:\DEPI\Medical Insurance Charges\output.png")

---

## 📬 Contact

For questions or contributions, open an issue or connect on [GitHub](https://github.com/AkramGamal1).
