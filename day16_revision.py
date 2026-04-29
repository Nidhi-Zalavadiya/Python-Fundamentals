# Step 1 — Load Data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Datasets/diabetes.csv")

print(df.shape)
print(df.info())
print(df.describe())
print(df.head(15))

# Step 2 — EDA
print(df.isnull().sum())

# with above find that there are no nan in any of column
# but in medical 0 means nan patiant can not have 0 bloodpressure

zero_columns = ["Glucose", "BloodPressure",
                "SkinThickness", "Insulin", "BMI"
                ]
for col in zero_columns:
    print(f"{col} : {(df[col]==0).sum()} Zeros")

# replace 0 with nan and then fill with median
for col in zero_columns:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

# correlation on heatmap
plt.figure(figsize=(10, 4))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt = ".2f"
)
plt.title("Diabetes — Correlation Matrix")
plt.tight_layout()
plt.savefig("images\day16_correlation.png")
plt.show()

# Step 3 — Feature Engineering 
df["glucose_bmi"] = df["Glucose"] * df["BMI"]
df["age_group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 45, 60, 100],
    labels=[0, 1, 2, 3]
).astype(int)
df["insulin_glucose"] = df["Insulin"] / (df["Glucose"] + 1)

# Train ALL 4 Models
feature_columns = [
    "Pregnancies", "Glucose", "glucose_bmi",
    "BloodPressure", "SkinThickness", "Insulin",
    "insulin_glucose", "BMI", "DiabetesPedigreeFunction",
    "Age", "age_group"
]

X = df[feature_columns]
y = df["Outcome"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale (needed for KNN and Logistic Regression)
scale = StandardScaler()
X_train_scale = scale.fit_transform(X_train)
X_test_scale = scale.transform(X_test)

models = {
    "KNN" : KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression" : LogisticRegression(max_iter=1000),
    "Decision Tree" : DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest" : RandomForestClassifier(n_estimators=100, random_state=42)
}

result = {}
for name, model in models.items():
    if "KNN" in name or "Logistic" in name:
        model.fit(X_train_scale, Y_train)
        pred = model.predict(X_test_scale)
    else:
        model.fit(X_train, Y_train)
        pred = model.predict(X_test)
    
    acc = accuracy_score(Y_test, pred)
    result[name] = acc, pred
    print(f"{name:30s} → {acc:.4f}")

# print(result)
# Step 5 — Best Model Deep Dive

# Take whichever model performed best
best_model = max(result)

# Print its full classification report
print(f"{best_model} Classification report : ")
print(classification_report(Y_test, result[best_model][1]))

# Print confusion matrix heatmap
cm = confusion_matrix(Y_test, result[best_model][1])

plt.figure(figsize=(10, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["NO Diabetes", "Has Diabetes"],
    yticklabels=["NO Diabetes", "Has Diabetes"]
)

plt.title(f"Diabetes - Confusion matrix {best_model}")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("images\day16_confusion_matrix_diabetes")
plt.show()

# Print feature importances (if Random Forest/DT)
if "random" in best_model.lower() or "dicision" in best_model.lower():
    importance = pd.Series(
        models[best_model].feature_importances_,
        index=feature_columns
    ).sort_values(ascending=False)

    plt.figure(figsize=(10, 5))
    importance.plot(kind="bar", color="forestgreen")
    plt.title(f"{best_model} — Feature Importance")
    plt.ylabel("Importance Score")
    plt.xlabel("Feature")
    plt.tight_layout()
    plt.savefig("images\day16_importance")
    plt.show()


# Step 6 — Comparison Chart
# Plot bar chart of all 4 model accuracies
# Color each bar differently
# Add title, labels, ylim
# Save as day16_comparison.png
accuracies = [v[0] for v in result.values()]
plt.figure(figsize=(8, 4))
plt.bar(
    result.keys(),
    accuracies,
    width=0.5,
    color=["orange", "coral", "cyan", "magenta"]
)
plt.title("Models Comparision Chart")
plt.xlabel("Model")
plt.tight_layout()
plt.savefig("images\day16_comparison")
plt.show()


# 1. What is the difference between fit() and transform()?
#    Why do we fit() on train but only transform() on test?
'''
    fit() -> Learn statistics from data(mean. std deviation)
    trasform() -> Applies thoese statistics to data
    fit_transform() = fit() + transform() together

    Imagine test data is "future unseen data"
    If you fit on test data too:
    Your scaler learns from future data
    That's like seeing tomorrow's exam answers today
    Called "data leakage" — model cheats without knowing

    scaler.fit_transform(X_train) 
    learns mean/std FROM training data
    scales training data using those values
    
    scaler.transform(X_test)
    uses SAME mean/std learned from training
    scales test data the same way
    
    Both train and test are now on same scale
    using only information the model "should" know
'''
# 2. Which model performed best on diabetes data?
#    Is that always the best model? Why/why not?
'''
    Random forest performed best on diabetes data
    No it is not always best model we can say it is best for nominal data
    for linear data logisting performance was better then random forest

'''
# 3. You got accuracy of X%. Is that good?
#    What else would you check besides accuracy?
#    (Think: what if 90% of patients don't have diabetes?)
'''
    confusion matrix numbers:
    TN = 82 (correctly said No Diabetes)
    FP = 17 (said Has Diabetes, actually No)
    FN = 18 (said No Diabetes, actually Has!) ← DANGEROUS
    TP = 37 (correctly said Has Diabetes)

    Imagine dataset: 900 healthy, 100 diabetic
    A DUMB model that always says "No Diabetes":
    Accuracy = 900/1000 = 90% ← looks amazing!
    But it catches ZERO actual diabetic patients!
    Completely useless medically!

    So besides accuracy check:
    Recall (most important for medical):
        = TP / (TP + FN) = 37 / (37+18) = 67%
        "Of all actual diabetic patients, 
        I correctly identified 67%"
        The 33% I missed could be deadly
        
    Precision:
        = TP / (TP + FP) = 37 / (37+17) = 69%
        
    For medical → Recall matters more
    Missing a sick person is worse than 
    a false alarm on a healthy person
'''

# 4. List the full ML pipeline in order (7 steps)
#    from raw data to final prediction.
'''
    1. load data sets
    2. EDA
    3. Feature Engineering
    4. Create Model
    5. Train Model
    6. Presict on Model
    7. Evalute Result
'''

# 5. What is the sklearn pattern that works for 
#    every single model? Write it from memory.
'''
    In sklearn commonaly follows four steps pattern:
    cerate model
    train model
    predict on model
    evalute result
'''