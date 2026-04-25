# Random Forest + Model Comparison
# Task A — Train Random Forest
'''
    fit()     → ALWAYS uses X_train, y_train
    predict() → ALWAYS uses X_test
    score()   → ALWAYS uses X_test, y_test
'''

import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# Load Data Set
data = sns.load_dataset("titanic")

df = data[[
    "survived", "pclass", "sex", "age", 
    "sibsp", "parch", "fare", "embarked"
]]

# fill null values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# encode data
df["sex"] = df["sex"].map({"male" : 0, "female" : 1})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

x = df.drop("survived", axis=1)
y = df["survived"]

X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

rf_model = RandomForestClassifier(
    n_estimators=100,
    oob_score=True,
    random_state=42
)

rf_model.fit(X_train, Y_train)
rf_pred = rf_model.predict(X_test)

print("Accuracy of random forest : ", accuracy_score(Y_test, rf_pred))
print("OOB (Out Of Bag) Score : ", rf_model.oob_score_)
print("Classification Report")
print(classification_report(Y_test, rf_pred))

#  Feature Importance
importances = pd.Series(
    rf_model.feature_importances_,
    index = x.columns
).sort_values(ascending=False)

plt.figure(figsize=(10,5))
importances.plot(kind="bar", color="forestgreen")
plt.title("Random Forest — Feature Importance")
plt.ylabel("Importance Score")
plt.xlabel("Feature")
plt.tight_layout()
plt.savefig("images\day13_rf_importance.png")
plt.show()

# Compare ALL 4 Models
models = {
    "KNN" : KNeighborsClassifier(n_neighbors=3),
    "Logistic Regression" : LogisticRegression(max_iter=1000),
    "Decision Tree" : DecisionTreeClassifier(
        max_depth=4, 
        random_state=42
    ),
    "Random Forest" : RandomForestClassifier(
        n_estimators=100,
        oob_score=True,
        random_state=42
    )
}

result = {}
for name, m in models.items():
    m.fit(X_train, Y_train)
    accuracy = accuracy_score(Y_test, m.predict(X_test))
    result[name] = accuracy
    print(f"Accuracy of {name:25s} : {accuracy:.4F}")

plt.figure(figsize=(8, 4))
plt.bar(
    result.keys(), 
    result.values(), 
    width=0.5,
    color=["steelblue","coral","orange","forestgreen"] 
)

plt.ylim(0.7, 0.9)
plt.ylabel("Accuracy")
plt.title("Model Comparison — Titanic Survival")
plt.tight_layout()
plt.savefig("images\day13_model_comparison.png")
plt.show()


# Why does Random Forest overfit less than a single Decision Tree?
'''
    in random forest it create multiple decision trees with their own
    unique features
    where in single decision tree it go depth depth
    with cause overfit
'''
# What is bootstrapping in plain English?
'''
    bootstrapping is like
    fisrt make parts and then agreegate
    is just like from single dataset
    we create different decision trees in random forest to make decision more efficient
    each single tree leanrs different pattern with it's
    randome sample rows and features
'''
# How many trees did you use and what accuracy did you get?
'''
    use 100 tree got accuracy 0.80 that is 80%
'''
# Which feature was most important according to Random Forest? Same as Decision Tree?
'''
    fare was most important feature in random forest
'''
# What is OOB score and why is it useful?
'''
    OOB score is 0.77 that is likely 77%
    it is random forest itself validation for remaining data 
    which are not use in train the model
'''
