# ML Task — Decision Tree on Titanic
# Task A 
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")

df = data[["survived", "pclass", "sex", "age", 
           "sibsp", "parch", "fare", "embarked"]]

df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df["sex"] = df["sex"].map({"male" : 0, "female" : 1})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

x = df.drop("survived", axis=1)
y = df["survived"]

X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Task B — Train with NO limit first
# Decision tree
model_full = DecisionTreeClassifier(random_state=42)
model_full.fit(X_train, Y_train)
predictions = model_full.predict(X_test)
print("Full Model Accuracy Score : ", accuracy_score(Y_test, predictions))
print("Full model depth : ", model_full.get_depth())

# Task C — Train with max_depth=4
# # Controlled depth
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, Y_train)
pred = model.predict(X_test)
print("Controlled Depth tree accuracy : ", accuracy_score(Y_test, pred))
print(classification_report(Y_test, pred))

# Task D — Feature Importance:
importances = pd.Series(
    model.feature_importances_,
    index=x.columns
).sort_values(ascending=False)

print(importances)


plt.figure(figsize=(8,4))
importances.plot(kind="bar", color="steelblue")
plt.title("Feature Importance — Decision Tree")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.savefig("day12_importance.png")
plt.show()

# Task E — Visualize the Tree
plt.figure(figsize=(18, 8))
plot_tree(
    model,
    feature_names=x.columns.tolist(),
    class_names=["Not Survived", "Survived"],
    filled=True,
    rounded=True,
    fontsize=9
)
plt.title("Decision Tree — Titanic (max_depth=4)")
plt.savefig("day12_tree.png", bbox_inches="tight")
plt.show()



# What is overfitting in plain English (your own words)?
'''
    overfitting is like models fullyunderstand train data 
    by asking all the possible questions which cuase
    it well understand training data but crash in new data

    just like i solve all the practice pragrams but
    fail to solve new problem which i didn't practice
'''
# What does max_depth=4 do to the tree?
'''
    max_depth=4 give limit to tree to ask q.s
    like with max_depth decision tree have 1 root node and
    3 internal node then final result directly
    no more extra q.s
'''
# Which feature was most important for survival prediction?
'''
    sex was the most important
'''
# What accuracy did you get with max_depth=None vs max_depth=4?
'''
    with max_depth=None i got 0.7877 is like 79% Accuracy
    and max_depth=4 i got 0.7988 is 0.80% Accuracy
'''
# Looking at the tree diagram — what was the ROOT question (very first split)?
'''
    sex <= 0.5
    gini = 0.469
    samples = 712
    value = [444, 268]
    class = Not Survived
'''