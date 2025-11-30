Mumbai House Price Prediction (Machine Learning Project)

This project predicts house prices in Mumbai using machine learning by analyzing property features, location factors, amenities, and furnishing levels. The workflow includes data cleaning, feature engineering, model training, performance comparison, and best model selection for accurate prediction.

Project Workflow

1️⃣ Load and Visualize Dataset
Understand price distribution and remove noise using exploratory data analysis (EDA).

2️⃣ Data Cleaning
Remove extreme outliers and ensure valid amenity values.

3️⃣ Feature Engineering
Create powerful features such as:
🔹 Price per Sqft
🔹 Total Amenities
🔹 Furnishing Score
🔹 Location-based price features
🔹 Log-transformed price

4️⃣ Feature Selection
Select the most meaningful predictors for efficient learning.

5️⃣ Train-Test Split & Scaling
Prepare data for training and avoid model bias.

6️⃣ Model Training & Evaluation
Models used:

Model	Type
Ridge Regression	Linear
Random Forest	Ensemble
Gradient Boosting	Boosting
XGBoost	Advanced Boosting

Evaluation metrics: R² Score, MAE, RMSE

7️⃣ Best Model Selection
The model with the highest R² Score (Log) is chosen as the final deployment model.

Technologies Used

Python

NumPy, Pandas

Matplotlib, Seaborn

Scikit-Learn

XGBoost

Pickle

Key Highlights

✔ Highly optimized feature engineering
✔ Multiple model comparison for best accuracy
✔ Handles price outliers and skewness
✔ Realistic performance metrics using original price scale

Future Scope

🔹 Deploy model as a web app (Streamlit/Flask)
🔹 Integrate real-time property data
🔹 Add rental price prediction support

Author

Rohit Dhole
