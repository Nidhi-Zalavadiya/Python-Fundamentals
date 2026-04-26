# Types of Feature Engineering
'''
    1. Handling Missing Values
    2. Encoding Feature Variables
    3. Feature Scalling
    4. Creating New Features
    5. Handling Outliers
'''
# ML Task — Feature Engineering on Titanic
# Task A — Create New Features
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")
data = data[["survived","pclass","sex","age",
         "sibsp","parch","fare","embarked"]]

# Basic cleaning
data["age"] = data["age"].fillna(data["age"].median())
data["embarked"] = data["embarked"].fillna(data["embarked"].mode()[0])
data["fare"] = data["fare"].fillna(data["fare"].median())

# NEW FEATURES — feature engineering
data["family_size"] = data["sibsp"] + data["parch"] + 1
data["is_alone"] = (data["family_size"] == 1).astype(int)
data["fare_per_person"] = data["fare"] / data["family_size"]
data["fare_log"] = np.log1p(data["fare"])

data["age_group"] = pd.cut(
    data["age"],
    # range pf bins to categorize age groups
    bins=[0, 12, 18, 35, 60, 100],
    labels=["child", "teen", "young", 'adult', 'senior']
)

print(
    data[["family_size", "is_alone", "fare_per_person",
            "fare_log", "age_group"  
        ]].head(10)
)


# Task B — Encode and Scale
# Encode categorical
data["sex"] = data["sex"].map({"male" : 0, "female" : 1})
data["age_group"] = data["age_group"].map({
    'child' : 0,
    'teen' : 1,
    'young' : 2,
    'adult' : 3,
    'senior' : 4
})

data = pd.get_dummies(data, columns=["embarked"], drop_first=True)

# Compare: model WITHOUT new features
X_basic = data[["pclass","sex","age","sibsp","parch","fare"]]
y = data["survived"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X_basic, y, test_size=0.2, random_state=42
)

rf_basic = RandomForestClassifier(n_estimators=100, random_state=42)
rf_basic.fit(X_train, Y_train)

acc_basic = accuracy_score(Y_test, rf_basic.predict(X_test))
print(f"Accuracy WITHOUT feature engineering: {acc_basic:.4f}")

# Task C — Model WITH new features + scaling
feature_cols = ["pclass","sex","age","sibsp","parch","fare",
                "family_size","is_alone","fare_per_person",
                "fare_log","age_group",
                "embarked_Q","embarked_S"
            ]
X_engineered = data[feature_cols]

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X_engineered, y, test_size=0.2, random_state=42
)

# Scale for KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train2)
X_test_scaled  = scaler.transform(X_test2)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, Y_train2)
acc_knn = accuracy_score(Y_test2, knn.predict(X_test_scaled))
print(f"KNN with scaling + new features: {acc_knn:.4f}")


rf_eng = RandomForestClassifier(n_estimators=100, random_state=42)
rf_eng.fit(X_train2, Y_train2)
acc_rf = accuracy_score(Y_test2, rf_eng.predict(X_test2))
print(f"Random Forest with new features: {acc_rf:.4f}")

# Task D — Visualize fare before and after log transform
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

data["fare"].hist(
    ax=axes[0],
    bins=40,
    color = "coral",
    edgecolor = "black"
)
axes[0].set_title(f"Fare (skew={data['fare'].skew():.2f})")
axes[0].set_xlabel("Fare")

data["fare_log"].hist(
    ax=axes[1],
    bins=40,
    color="steelblue",
    edgecolor = "black"
)
axes[1].set_title(f"log(Fare) (skew={data['fare_log'].skew():.2f})")
axes[1].set_xlabel("log Fare")

plt.tight_layout()
plt.savefig("images\day15_fare_transform.png")
plt.show()

# Task E — Feature importance with new features
importance = pd.Series(
    rf_eng.feature_importances_,
    index=feature_cols
).sort_values(ascending=False)

plt.figure(figsize=(10, 5))
importance.plot(kind="bar", color="forestgreen")
plt.title("Feature Importance — After Feature Engineering")
plt.tight_layout()
plt.savefig("images\day15_importance.png")
plt.show()

print("\nFare skewness before:", data["fare"].skew())
print("Fare skewness after log:", data["fare_log"].skew())


# Why does KNN need feature scaling but Decision Tree doesn't?
'''
    KNN uses distance where distance between number can be bigger
    where decision tree make decision based on condition 
    so there is no need of scalling in desion tree and random forest
'''
# What is the difference between Label Encoding and One-Hot Encoding?
'''
    one-hot encoding creates new binary column for every unique category
    where label encoding encode categorical data into one single column
    it is memory efficient 
'''
# After adding family_size and is_alone — did accuracy improve?
'''
    yes
'''
# What did the log transform do to the fare distribution skewness?
'''
    please explain
'''
# Which new feature you created had the highest importance score?
'''
    fare log
'''