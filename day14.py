# ML Task — Full EDA on Titanic
# Task A — Basic Info

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")

print("shape : ", data.shape)
print("info : ")
print(data.info())
print("Describe : ")
print(data.describe())
print("Missing Value")
print(data.isnull().sum())

# Task B — Missing Values Heatmap
plt.figure(figsize=(10, 4))
sns.heatmap(
    data.isnull(),
    cbar=False,
    cmap="viridis",
    yticklabels=False
)
plt.title("Missing Values Map (Yellow = Missing)")
plt.tight_layout()
plt.savefig("images\day14_missing.png")
plt.show()

# Task C — Distribution of Numerical Features
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

data["age"].hist(ax=axes[0, 0], bins=20, color="steelblue", edgecolor="black")
axes[0,0].set_title("Age Distribution")

data["fare"].hist(ax=axes[0, 1], bins=30, color="coral", edgecolor="black")
axes[0, 1].set_title("Fare Distribution")

data["pclass"].value_counts().sort_index().plot(
    kind="bar", ax=axes[0, 2], color="orange"
)
axes[0,2].set_title("Passenger Class Count")

data["sibsp"].value_counts().sort_index().plot(
    kind="bar", ax=axes[1, 0], color="green"
)
axes[1,0].set_title("Siblings/Spouses Count")

data["survived"].value_counts().sort_index().plot(
    kind="bar", ax=axes[1, 1], color=["red", "green"]
)
axes[1,1].set_title("Survived Count")

data.boxplot(column="fare", by="pclass", ax=axes[1, 2])
axes[1,2].set_title("Fare by Passenger Class")

plt.tight_layout()
plt.savefig("images\day14_distributions.png")
plt.show()

# Task D — Correlation Heatmap
data_encoded = data.copy()

data_encoded["sex"] = data_encoded["sex"].map({"male" : 0, "female" : 1})

num_column = ["survived", "pclass", "age",
              "sex", "sibsp", "parch", "fare"
              ]
corr = data_encoded[num_column].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f",
    square=True
)

plt.tight_layout()
plt.savefig("images\day14_correlation.png")
plt.show()

# Task E — Survival Analysis
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Survival by sex
data.groupby("sex")["survived"].mean().plot(
    kind="bar", ax=axes[0], color=["coral","steelblue"]
)

axes[0].set_title("Survival Rate by Sex")
axes[0].set_ylabel("Survival Rate")

# Survival by pclass
data.groupby("pclass")["survived"].mean().plot(
    kind="bar", ax=axes[1], color="purple"
)
axes[1].set_title("Survival Rate by Class")

# Age distribution by survival
data[data["survived"]==1]["age"].hist(
    ax=axes[2], alpha=0.6, label="Survived", 
    color="green", bins=20
)
data[data["survived"]==0]["age"].hist(
    ax=axes[2], alpha=0.6, label="Not Survived", 
    color="red", bins=20
)
axes[2].legend()
axes[2].set_title("Age Distribution by Survival")

plt.tight_layout()
plt.savefig("images\day14_survival_analysis.png")
plt.show()

# Skewness check
print("Fare skewness:", data["fare"].skew())
print("Age skewness:",  data["age"].skew())

# Which two features are most correlated with each other?
'''
    sex and survived are most correlated with each other
'''

# Which feature has the most outliers based on boxplot?
'''
    fare
'''
# Which feature shows the clearest separation between survived=0 and survived=1 in the pairplot?
'''
    sex
'''
# What is the skewness of the fare column? (use df["fare"].skew())
'''
    4.787
'''
# What does a correlation of -1 mean in plain English?
'''
    correlation -1 means one is up and another goes down
    like in survived we can say correlation between
    age and survived
    with example there is x and y
    when x goes up y downs
'''