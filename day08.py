import pandas as pd
import numpy as np

# Task 1 — Pandas merge, sort, pivot 
# A
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

student = pd.DataFrame(data)

# Sorting — 4 operations on the student DataFrame
# Sort by python_score descending.

student_by_python_score = student.sort_values(by = "python_score", ascending=False)
print(student_by_python_score)

#  Sort by city ascending then python_score descending — two columns at once.
student_by_city_python_score = student.sort_values(by = ["city", "python_score"], ascending=[True, False])
print(student_by_city_python_score)

# Find top 3 students by total score.
student["total_score"] = student["python_score"] + student["ml_score"]
top = student.nlargest(3, ['total_score'], )
print("Top 3 : ", top.head(3))

# Find the bottom 2 students by ml_score. Use df.sort_values() — figure out the parameters yourself from what you know.
bottom_two = student.sort_values(by = "ml_score", ascending = False)
print(bottom_two.tail(2))



# B
# Merge two DataFrames — like SQL JOIN
# Create two DataFrames: one with student names and scores, 
# one with student names and their city and phone number.

data_score = {
    "name" : ["Raj", "Priya", "Amit", "Nidhi", "Arjun",
                "Pooja", "Karan", "Sneha", "Vivek", "Riya"],
    "scores" : [85, 92, 78, 88, 65, 91, 74, 83, 69, 95]
}

student_score = pd.DataFrame(data_score)

data_details = {
    "name" : ["Radhika", "Priya", "Amit", "Nidhi", "Arjun",
                "Pooja", "Karan", "Snehal", "Vivek", "Riyansh"],
    "city":    ["Junagadh", "Ahmedabad", "Junagadh", "Surat",
                "Ahmedabad", "Junagadh", "Surat", "Ahmedabad",
                "Junagadh", "Surat"],
    "phone_number" : [
        9958695645, 8689564151, 9465825478, 8956535651, 7856859658,
        8856548946, 7658598965, 6566859658, 9965663748, 9135689896
    ]
}

student_details = pd.DataFrame(data_details)

#  Merge them on the "name" column using inner join. 
merge_on_name = pd.merge(student_score, student_details, how="inner", on="name")
print(merge_on_name)

# Then try left join — observe what changes when a name exists in one DataFrame but not the other. 
left_join_students = pd.merge(student_score, student_details, how="left")
print(left_join_students)

# Write a comment explaining the difference between inner and left join.
'''
    with inner join on name it gives the data that are exist in both the dataframes
    it is act like intersection select those which exist in both

    in left join it give data of whole left/first dataframe but 
    from right/second dataframe only return that are same exist in left dataframe

    inshort left join perform operation by collecting exist in left on both the data frames

'''


# C
# Apply a custom function to a column
# Use df["column"].apply(function) to create a new column "score_category" 
# from python_score: "Excellent" if score >= 90, 
# "Good" if 75-89, "Average" if 60-74, "Poor" below 60.
# def find_catagory(score):
#     if score >= 90:
#         return "Excellent"
#     elif score <= 89 and score >= 75:
#         return "Good"
#     elif score <= 74 and score >= 60:
#         return "Average"
#     else:
#         return "Poor"
    
# Cleaner — trust the elif chain
def find_category(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:    # already know < 90
        return "Good"
    elif score >= 60:    # already know < 75
        return "Average"
    else:
        return "Poor"
student["score_category"] = student["python_score"].apply(find_category)
print(student)
#  Write a regular function first, then rewrite it as a lambda.
student["score_category1"] = student["python_score"].apply(
    lambda score : "Excellent" if score >= 90 else "Good" if score >= 75 else "Average" if score >= 60 else "Poor"
    )
print(student)
#  Both must produce identical output.


# D
# Pivot table — summarise data like Excel
import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = sns.load_dataset("titanic")
# Using the Titanic dataset:
#  create a pivot table showing average survival rate for each combination of pclass and sex.
#  Use pd.pivot_table() with values="survived", index="pclass", columns="sex", aggfunc="mean". 
# This single table shows the most important survival pattern in the dataset.
survival_rate_pivot = pd.pivot_table(
        data = titanic_data,
        index = "pclass", 
        columns = "sex",
        values = "survived",
        aggfunc = "mean"
    )

print(survival_rate_pivot)


# Task 2 — Matplotlib visualisation 
# A
# 4 charts on the student data — one of each type
# Bar chart: average python_score per city.

plt.figure(figsize=(17, 4)) 

avg_by_city = student.groupby("city")["python_score"].mean()
plt.subplot(141)
plt.bar(avg_by_city.index, avg_by_city.values)
plt.xlabel("City")
plt.ylabel("Python score")
plt.title("Average python_score per city")
# plt.show()

# Line chart: plot python_score and ml_score side by side for all 10 students — use student names as x-axis. 
plt.subplot(142)
plt.plot(student.index, student["python_score"], "b--", label = "Pyton Score")
plt.plot(student.index,student["ml_score"], "g--", label = "ml_Score")
plt.legend()
plt.xlabel("Student")
plt.ylabel("Score")
plt.title("Average python_score per city")
# plt.show()

# Scatter plot: python_score on x-axis, ml_score on y-axis — each dot is one student.
plt.subplot(143)
#  s is dot size in scatter function
plt.scatter(student["python_score"], student["ml_score"], s = 80, linewidths=5.0 ,marker="o", label = "Student")
plt.xlabel("Python Score")
plt.ylabel("ML Score")
plt.legend()
plt.title("Score of Students")
# plt.show()

# Histogram: distribution of all scores — use np.concatenate to combine python and ml scores into one array. 
scores = np.concatenate((student["python_score"] , student["ml_score"]), dtype="int")
plt.subplot(144)
plt.hist(scores, bins=5, color="blue", edgecolor = "black", label="Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Scores")
plt.savefig("images\Student Data Analisys")
plt.show()
# Each chart needs title, xlabel, ylabel.

# B
# Titanic survival chart using Seaborn
# Use seaborn which gives better looking charts with less code. 
# Create: a countplot showing survived vs not survived split by sex.
# Use sns.countplot(data=df, x="survived", hue="sex"). Add a title. 
sns.countplot(data = titanic_data, x = "survived", hue="sex")
plt.title("Titanic survival by Gender")
plt.savefig("images\\titanic_survival.png")
plt.show()  

# Task 3 — Kaggle setup
df = pd.read_csv("train.csv")
print(df.info())
print(df.describe())
'''
    in this dataset there are 80 columns with different data types 
    like float, int, str
    There are missing values in alley, MasVnrType, MasVnrArea etc..
'''