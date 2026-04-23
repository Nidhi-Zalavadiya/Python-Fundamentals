# THE SCIKIT-LEARN PATTERN 
# from sklearn.ModelFamily import ModelName

# model = ModelName()          # 1. Create
# model.fit(X_train, y_train)  # 2. Train
# model.predict(X_test)        # 3. Predict
# model.score(X_test, y_test)  # 4. Evaluate

# Task A — Setup & Explore:
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["species"] = df["target"].map({0:"setosa", 1:"versicolor", 2:"virginica"})

print(df.head(10))
print(df.describe())
print(df["species"].value_counts())


# Task B — Train your FIRST ML model:
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X = df[iris.feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

# Task C — Visualize:
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"],
            c=df["target"], cmap="viridis")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris — Sepal Features")

plt.subplot(122)
plt.scatter(df["petal length (cm)"], df["petal width (cm)"],
            c=df["target"], cmap="viridis")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Iris — Petal Features")

plt.tight_layout()
plt.savefig("images\day09_iris.png")
plt.show()

# 1. What does test_size=0.2 mean in simple words?
'''
    test_size=0.2 means size of data on which model test is 20% of whole data
'''
# 2. What happens if you change n_neighbors=3 to n_neighbors=1? Try it.

# 3. What happens if you change n_neighbors=3 to n_neighbors=10? Try it.
'''
    Nothing Changeboth tthe time or i don't understand it's concept yet
    explain me neighbors concept in plain english first or give me 
    matirial link like w2school or gfg or real python or official doc
 '''
# 4. Why do we need to separate X and y?
'''
    we need separate x and y to train model on data x and
    predict on data y
    if we won't split the data then there is no point to make 
    predictions model already have whole data

'''
# 5. What accuracy did you get?
'''
    got Accuracy 1.0
'''