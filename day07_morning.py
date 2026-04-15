# Task 1 — DataFrame basics 
# A Create and explore a DataFrame
import pandas as pd
import numpy as np

# Create from dictionary — most common way
data = {
    "name":    ["Raj", "Priya", "Amit", "Nidhi", "Arjun",
                "Pooja", "Karan", "Sneha", "Vivek", "Riya"],
    "age":     [21, 22, 20, 21, 23, 22, 20, 21, 24, 22],
    "city":    ["Junagadh", "Ahmedabad", "Junagadh", "Surat",
                "Ahmedabad", "Junagadh", "Surat", "Ahmedabad",
                "Junagadh", "Surat"],
    "python_score": [85, 92, 78, 88, 65, 91, 74, 83, 69, 95],
    "ml_score":     [78, 88, 65, 90, 72, 85, 68, 79, 71, 93],
    "experience":   [1, 2, 0, 1, 3, 2, 0, 1, 2, 3]
}

df = pd.DataFrame(data)

# Explore — run each line and observe the output
print(df)               # full table
print(df.head(3))       # first 3 rows
print(df.tail(3))       # last 3 rows
print(df.shape)         # (rows, columns)
print(df.dtypes)        # data type of each column
print(df.info())        # summary — shape, dtypes, nulls
print(df.describe())    # statistics for numeric columns

# Write a comment: what does df.describe() show?
'''
    df.info() shows the information about dataframe
    like column name with it's datatype , rangeindex, type of object, no.of column,
    memory usage etc.
'''
# What is the difference between df.info() and df.describe()?
'''
    Difference between d.info() and df.describe()
    is that df.info() give the information about dataframe
    with it's datatypes. object type, memory usage, shape etc

    wehere df.describe() gives the statistic operations on numaric columns
    like mean, count, std, etc.. for each column
'''


# B Selecting data — 8 operations
# Column selection
print(df["name"])                        # one column — returns Series
print(df[["name", "python_score"]])      # multiple columns — returns DataFrame

# Row selection with loc and iloc
# Retrun first row
print(df.loc[0])                         # row by label
# Return first row
print(df.iloc[0])                        # row by position
print(df.loc[2:5, "name":"python_score"])# rows 2-5, columns name to python_score
print(df.iloc[0:3, 0:3])                # first 3 rows, first 3 columns

# Boolean filtering — most used in real data work
print(df[df["python_score"] > 80])      # students with score above 80
print(df[df["city"] == "Junagadh"])     # only Junagadh students

# Multiple conditions — & means AND, | means OR
print("multiple condition")
# return where python score > 80 and also city = junagadh meet both condition
print(df[(df["python_score"] > 80) & (df["city"] == "Junagadh")])
# return where python score > 90 or ml_score > 90 whatever condition meet
print(df[(df["python_score"] > 90) | (df["ml_score"] > 90)])

# For each result — write what you expect before running
# Then verify by running



# C Adding and modifying columns
# Add a new column — total score
df["total_score"] = df["python_score"] + df["ml_score"]

# Add a calculated column — average score
df["avg_score"] = (df["python_score"] + df["ml_score"]) / 2

# Add a categorical column using condition
df["level"] = np.where(df["avg_score"] >= 85, "Senior", "Junior")

# Add grade column using multiple conditions
conditions = [
    df["avg_score"] >= 90,
    df["avg_score"] >= 80,
    df["avg_score"] >= 70,
]
grades = ["A", "B", "C"]
df["grade"] = np.select(conditions, grades, default="F")

print(df[["name", "python_score", "ml_score",
          "total_score", "avg_score", "level", "grade"]])

# Modify existing column — add 5 bonus marks to everyone in ml_score
df["ml_score"] = df["ml_score"] + 5
print(df[["name", "ml_score"]].head())


# Task 2 — Data cleaning and groupby 
# A Handle missing data — the most common real-world problem

# Create a messy dataset with missing values
messy_data = {
    "name":         ["Raj", "Priya", None, "Nidhi", "Arjun"],
    "age":          [21, None, 20, 21, 23],
    "score":        [85, 92, None, 88, None],
    "city":         ["Junagadh", "Ahmedabad", "Junagadh", None, "Ahmedabad"],
}
df_messy = pd.DataFrame(messy_data)

print(df_messy)
print("\nMissing values per column:")
print(df_messy.isnull().sum())       # count nulls per column
print("\nAny nulls?", df_messy.isnull().any().any())

# Fix missing values — 3 strategies
# Strategy 1: drop rows with any missing value
df_dropped = df_messy.dropna()
print("\nAfter dropping nulls:", df_dropped.shape)

# Strategy 2: fill with a fixed value
df_filled = df_messy.fillna({
    "name":  "Unknown",
    "city":  "Unknown",
    "age":   df_messy["age"].mean(),    # fill age with average age
    "score": df_messy["score"].median() # fill score with median score
})
print("\nAfter filling nulls:")
print(df_filled)

# Strategy 3: forward fill — use previous row's value
df_ffill = df_messy.ffill()
print("\nForward fill:")
print(df_ffill)

# Remove duplicate rows
df_with_dupes = pd.concat([df_messy, df_messy.iloc[0:2]])
print("\nWith duplicates:", df_with_dupes.shape)
df_clean = df_with_dupes.drop_duplicates()
print("After removing duplicates:", df_clean.shape)


# B groupby — the most powerful Pandas operation

# Use the student df from Task 1
data = {
    "name":    ["Raj","Priya","Amit","Nidhi","Arjun",
                "Pooja","Karan","Sneha","Vivek","Riya"],
    "city":    ["Junagadh","Ahmedabad","Junagadh","Surat",
                "Ahmedabad","Junagadh","Surat","Ahmedabad",
                "Junagadh","Surat"],
    "python_score": [85,92,78,88,65,91,74,83,69,95],
    "ml_score":     [78,88,65,90,72,85,68,79,71,93],
    "experience":   [1,2,0,1,3,2,0,1,2,3]
}
df = pd.DataFrame(data)

# groupby — split into groups, apply function, combine
# "For each city, calculate..."

# Average python score per city
print(df.groupby("city")["python_score"].mean())

# Multiple statistics at once
print(df.groupby("city")["python_score"].agg(["mean","min","max","count"]))

# Group by city, get stats for ALL numeric columns
print(df.groupby("city").mean(numeric_only=True))

# Count students per city
print(df.groupby("city").size())

# Who is the top scorer in each city?
print(df.loc[df.groupby("city")["python_score"].idxmax()])

# Write a comment explaining:
# What does groupby actually do step by step?
# Think: Split → Apply → Combine
'''
    firstly groupby group data by given series like in our example
    it is group by city
    saperate data by city and then one by one apply given functions to it
    then combine all the result 
'''


# Mini project — analyse a real dataset (7:50–8:30 AM)
# Download and analyse the Titanic dataset
# Download Titanic dataset — paste this in terminal:
# pip install seaborn
# Then in Python:
import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("titanic")   # loads directly, no CSV needed
print(df.shape)
print(df.head())
print(df.isnull().sum())           # see which columns have missing data

# Answer these 8 questions — no loops, pandas only:

# 1. How many passengers survived vs did not survive?
#    (use value_counts())
survived_or_not = df["servived"].value_counts()
print(f"survived : {survived_or_not[1]}, not servived : {survived_or_not[0]}")

# 2. What was the survival rate (%) by passenger class (pclass)?
#    Hint: groupby pclass, mean of survived column
survived_rate = df.groupby("pclass")["survived"].mean()
print(survived_rate)

# 3. What was the average age of survivors vs non-survivors?
age = df.groupby("survived")["age"].mean()
print(f"Average age of Survived : {age[1]}, \n Average age of non survived : {age[0]}")

# 4. How many males and how many females were on board?
count_male_female = df.value_counts(df["sex"])
print(count_male_female)

# 5. What percentage of females survived vs males?
#    This is the most important insight in this dataset
survie = df.groupby("sex")["survived"].mean()
print(survie)

# 6. Fill missing age values with the median age
#    Do not drop rows — fill them
df["age"] = df["age"].fillna({
    "age" : df["age"].median(),
})
print(df)

# 7. Create a new column "age_group":
#    "Child" if age < 18
#    "Adult" if age 18-60
#    "Senior" if age > 60
#    Use np.select — no loops
print(df[(df["age"] >= 18) & (df["age"] <= 60)])
condition = [
    df["age"] < 18,
    (df["age"] >= 18) & (df["age"] <= 60),
    df["age"] > 60
]

group = ["Child", "Adult", "Senior"]

df["age_group"] = np.select(condition, group, default="Adult")
print(df.head(10))

# 8. What is the survival rate for each age_group?
#    Use groupby
survival_rate = df.groupby("age_group")["survived"].mean()
print(survival_rate)


print("\n--- Analysis complete ---")