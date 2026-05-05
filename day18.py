# Feature Scaling
# Load Titanic. 
# Pick Age and Fare. 
# Apply StandardScaler — print mean and std before and after. 
# Then apply MinMaxScaler — observe the range becomes 0 to 1.
# Hint: StandardScaler makes mean=0, std=1. 
# MinMaxScaler squeezes everything into [0,1]. 
# KNN and SVM need scaling — Decision Trees don't. 
# Ask yourself why.


import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load the Titanic dataset
data = sns.load_dataset("titanic")

# Understand the data
print(data.shape)
print(data.describe())
print(data.info())
print(data.isnull().sum())

data = data[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']]

num_cols = ['age', 'fare', 'pclass']
cat_cols = ['embarked', 'sex']

print("Before Scaling:")
print(f"Age Mean : {data['age'].mean()}, Age Std : {data['age'].std()}")
print(f"Fare Mean : {data['fare'].mean()}, Fare Std : {data['fare'].std()}")


X = data.drop('survived', axis=1)
y = data['survived']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

num_pipeline = Pipeline([
    ('impute', SimpleImputer(strategy='median')),
    ('scale', StandardScaler())
])

cat_pipeline = Pipeline([
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('encode', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])


full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression(max_iter=500, random_state=42))
])

# Fit the pipeline to the training data
full_pipeline.fit(X_train, Y_train)

# Extract the scaler from the pipeline
scaler = full_pipeline.named_steps['preprocessor']\
    .named_transformers_['num']\
    .named_steps['scale']

# After Standard Scaling
print("\nAfter Standard Scaling:")
print(f'Age mean : {scaler.mean_[0]}, Age std : {scaler.scale_[0]}')
print(f'Fare mean : {scaler.mean_[1]}, Fare std : {scaler.scale_[1]}')

train_acc = full_pipeline.score(X_train, Y_train)
test_acc = full_pipeline.score(X_test, Y_test)
print(f"\nLogistic Regression Train Accuracy: {train_acc:.4f}")
print(f"Logistic Regression Test Accuracy: {test_acc:.4f}")


# KNN without scaling
X_num = data[['age', 'fare']].fillna(data[['age', 'fare']].median())

X_train_num, X_test_num, Y_train_num, Y_test_num = train_test_split(
    X_num, y, test_size=0.2, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_num, Y_train_num)
print(f"\nKNN Accuracy without Scaling: {knn.score(X_test_num, Y_test_num):.4f}")


#  Fare has extreme outliers (some tickets cost 500+) — StandardScaler doesn't handle outliers well.
scaler_knn = StandardScaler()
X_train_scalesd = scaler_knn.fit_transform(X_train_num)
X_test_sclaed = scaler_knn.transform(X_test_num)

knn2 = KNeighborsClassifier(n_neighbors=5)
knn2.fit(X_train_scalesd, Y_train_num)
print(f"KNN Accuracy with Standard Scaling: {knn2.score(X_test_sclaed, Y_test_num):.4f}")


#  RobustScaler is more robust to outliers — it uses median and IQR instead of mean and std.
robust_scaler = RobustScaler()
x_train_robust = robust_scaler.fit_transform(X_train_num)
X_test_robust = robust_scaler.transform(X_test_num)

knn3 = KNeighborsClassifier(n_neighbors=5)
knn3.fit(x_train_robust, Y_train_num)
print(f"KNN Accuracy with Robust Scaling: {knn3.score(X_test_robust, Y_test_num):.4f}")