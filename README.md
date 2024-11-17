# Loan Approval Prediction using SVM 🤖💳

Welcome to the **Loan Approval Prediction** project! In this repository, I have built a machine learning model using **Support Vector Machine (SVM)** to predict whether a loan application will be approved or not based on various features such as applicant's income, credit score, loan amount, and more.

The project includes an **Exploratory Data Analysis (EDA)** and **data preprocessing** steps to understand and prepare the data for training. Additionally, I have developed a **Streamlit web app** that allows users to input loan application details and predict the approval status.

---

## 📂 Repository Contents

- **SVM.ipynb**  
  Jupyter Notebook containing the implementation of the loan approval prediction model using **SVM**. The notebook includes steps for EDA, preprocessing, model training, and evaluation.

- **app.py**  
  A Streamlit app that serves as a simple web interface for the loan approval prediction model. Users can enter application details, and the app will predict the loan approval status.

- **data.csv**  
  This csv file containins the dataset used for training the SVM model. The dataset includes various features like income, credit score, loan amount, etc.

- **requirements.txt**  
  A file listing the required Python libraries for running the scripts (e.g., `scikit-learn`, `pandas`, `streamlit`, `matplotlib`).

---

## 🎯 Project Overview

1. **Exploratory Data Analysis (EDA)**  
   - I performed EDA to understand the data distribution, check for missing values, visualize relationships between variables, and identify important features influencing loan approval.

2. **Data Preprocessing**  
   - The dataset was cleaned and transformed by handling missing values, encoding categorical variables, and scaling numerical features.
   - I used techniques like **Label Encoding**, **Imputation**, and **Standardization** to prepare the data for modeling.

3. **Modeling**  
   - I used the **Support Vector Machine (SVM)** algorithm to train a model that predicts loan approval. The model was evaluated using **accuracy**, **precision**, and **recall** to ensure it provides reliable predictions.

4. **Streamlit Web App**  
   - I created a simple and interactive **Streamlit** app, allowing users to enter loan application details and get an immediate prediction about the approval status of the loan.

---

## 🛠️ How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ThisIsFarhan/Loan-Approval-Engine.git
