import seaborn as sns
import pandas as pd

data = sns.load_dataset("titanic")

df = data[["survived", "pclass", "sex", "age", 
           "sibsp", "parch", "fare", "embarked"]]

# age → has nulls → fill with median age
#   embarked → has nulls → fill with most common port
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# Text to numbers:
#   sex: male/female → 0/1  (model can't read text)
#   embarked: C/Q/S → 0/1/2
df["sex"] = df["sex"].map({"male" : 0, "female" : 1})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

print(df.head())
print(df.isnull().sum())   
print(df.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Split X and y
x = df.drop("survived", axis=1)
y = df["survived"]

# train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# LogisticRegression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Predict
predictions = model.predict(X_test)

# accuracy_score
print("Accuracy Score : ", accuracy_score(Y_test, predictions))

# classification_report
print("Classification Report : \n", classification_report(Y_test, predictions))


# confusion_matrix
cm = confusion_matrix(Y_test, predictions)
print("Confusion Matrix : \n", cm)

# Visualize confusion matrix as heatmap
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Not Survived", "survived"],
            yticklabels=["Not Survived", "survived"]
            )
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Titanic — Confusion Matrix")
plt.tight_layout()
plt.savefig("images\day11_confusion_matrix.png")
plt.show()


# What is the difference between Logistic and Linear Regression in one line?
'''
    The difference between logistic and linear regression is that
    linear regression predict a number which match the most where 
    logist regression predict probability, and converts to yes/no
'''
# What does a False Negative mean in the Titanic context?
'''
    False negative means positive that is
    survived in actule and not survived in predict
'''

# Your model's precision vs recall — which is higher and what does that mean?
'''
    TN = 90  (predicted Not Survived, actually Not Survived ✅)
    FP = 15  (predicted Survived,     actually Not Survived ❌)
    FN = 19  (predicted Not Survived, actually Survived     ❌)
    TP = 55  (predicted Survived,     actually Survived     ✅)

    Precision = TP / (TP + FP) = 55 / (55+15) = 55/70 = 0.79
    → "When I said someone survived, I was right 79% of time"

    Recall    = TP / (TP + FN) = 55 / (55+19) = 55/74 = 0.74
    → "Of all people who actually survived, I caught 74% of them"

    Precision > Recall in your model (0.79 > 0.74)
    This means your model is more careful about 
    WHO it calls a survivor, but misses some real survivors
'''
# Why did we fill missing age with median and not mean?
'''
    Imagine ages: [1, 2, 3, 4, 100]

    Mean   = (1+2+3+4+100)/5 = 22  ← pulled up by 100 (outlier)
    Median = 3                      ← middle value, not affected

    Titanic had very old and very young passengers
    A few extreme ages (outliers) would pull the mean
    away from what a "typical" passenger age looks like

    Median is more ROBUST to outliers
    That's why we always prefer median for age/salary data
'''

# What accuracy did you get?
'''
    i got 81% Accuracy that is 0.81
'''