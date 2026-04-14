# Task 1 — Array creation and properties 
# A Create arrays 6 different ways — understand each one
import numpy as np

def atributes(arr):
    print("operations on ", arr)
    print(arr.shape, "Shape")
    print(arr.dtype, "DataType")
    print(arr.ndim, "Dimensions")
    print(arr.size, "Size")
# 1. From a Python list
arr1 = np.array([10, 20, 30, 40, 50])

# 2. Range of numbers — like Python range() but returns array
arr2 = np.arange(0, 20, 2)      # 0 to 20, step 2
arr3 = np.linspace(0, 1, 5)     # 5 evenly spaced numbers from 0 to 1

# 3. Special arrays
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones  = np.ones(5)                # [1. 1. 1. 1. 1.]
empty = np.empty(5)              # uninitialized — random junk values

# 4. 2D arrays (matrices)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

identity = np.eye(3)             # identity matrix — 1s on diagonal
# print(identity)

# 5. Random arrays
rand_arr  = np.random.rand(5)         # 5 random floats between 0 and 1
rand_int  = np.random.randint(1, 100, size=5)  # 5 random ints 1-100
rand_norm = np.random.randn(5)        # 5 numbers from normal distribution

# For each array above — print these 4 things:
# print(arr.shape)    # dimensions
# print(arr.dtype)    # data type
# print(arr.ndim)     # number of dimensions
# print(arr.size)     # total number of elements
# Do this for: arr1, matrix, rand_norm

atributes(arr1)
atributes(arr2)
atributes(arr3)

atributes(zeros)
atributes(ones)
atributes(empty)

atributes(matrix)

atributes(rand_arr)
atributes(rand_int)
atributes(rand_norm)

# Write what you observe as a comment
'''
   arr1 output 
    operations on  [10 20 30 40 50]
    (5,) Shape
    int64 DataType
    1 Dimensions
    5 Size

    On matrix
    operations on  [[1 2 3]
    [4 5 6]
    [7 8 9]]
    (3, 3) Shape
    int64 DataType
    2 Dimensions
    9 Size

    rand_norm with this 
    operations on  [ 0.61579499 -2.13616731  0.26425572  0.20051886 -2.08522079]
    (5,) Shape
    float64 DataType
    1 Dimensions
    5 Size

    arr1 is 1 dimension array with 1 axis
    size id no. of elements

    matrix is 2 dimension array with 2 axis
    size if no. of rows * column

    rand_norm is one dimension array generated with random flot value
    size if no. of elements

'''

# B Indexing and slicing — same as lists but more powerful


arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 1D slicing — same as Python lists
print(arr[0])        # first element
print(arr[-1])       # last element
print(arr[2:6])      # elements at index 2,3,4,5
print(arr[::2])      # every other element

# 2D indexing — this is NEW compared to lists
matrix = np.array([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12]])

print(matrix[0])         # entire first row
print(matrix[:, 0])      # entire first column — : means all rows
print(matrix[1, 2])      # row 1, column 2 — single element
print(matrix[0:2, 1:3])  # rows 0-1, columns 1-2 — submatrix

# Boolean indexing — most important for ML data filtering
scores = np.array([85, 42, 90, 55, 78, 38, 95, 61])

# Print only scores above 70
print(scores[scores > 70])

# Replace all scores below 60 with 0
scores[scores < 60] = 0
print(scores)

# How many students passed (score > 70)?
print(np.sum(scores > 70))


# Task 2 — Array operations 
# A Vectorised operations — no loops needed

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Element-wise math — predict output FIRST, then run
print(a + b)       # ? [11, 22, 33, 44, 55]
print(a * b)       # ? [10, 40, 90, 160, 250]
print(b / a)       # ? [10, 10, 10, 10, 10]
print(a ** 2)      # ? [1, 4, 9, 16, 25]
print(np.sqrt(b))  # ? [3.16, 4.47, 5.47, 6.32, 7.07]

# Broadcasting — adding a scalar to an array
print(a + 100)     # adds 100 to every element
print(a * 3)       # multiplies every element by 3

# This is ML normalisation in 1 line:
raw_scores = np.array([85.0, 42.0, 90.0, 55.0, 78.0])
mean  = raw_scores.mean()
std   = raw_scores.std()
normalised = (raw_scores - mean) / std   # Z-score normalisation
print(normalised)
# Values close to 0 mean near average
# Positive means above average, negative means below
# This exact formula is used in every ML preprocessing step

# explain me what does above formula exactly does and where it is used in ml


# B Statistics functions — the ones used in ML daily

data = np.array([23, 45, 12, 67, 34, 89, 56, 78, 43, 21])

# Basic statistics — use NumPy functions, not Python built-ins
print("Mean   :", data.mean())       # average
print("Median :", np.median(data))   # middle value
print("Std    :", data.std())        # spread of data
print("Var    :", data.var())        # variance = std squared
print("Min    :", data.min())
print("Max    :", data.max())
print("Sum    :", data.sum())
print("Range  :", data.max() - data.min())

# For a 2D array — axis matters
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.sum())           # sum of ALL elements
print(matrix.sum(axis=0))     # sum of each COLUMN — [12, 15, 18]
print(matrix.sum(axis=1))     # sum of each ROW — [6, 15, 24]
print(matrix.mean(axis=0))    # average of each column


# please explain me standard deviation i see everywhere but stil don't understand

# Write a comment explaining: what does axis=0 mean vs axis=1?
# This is asked in interviews and comes up constantly in pandas too
'''
    axis=0 means column
    and axis=1 is rows
'''


# C Reshape and stack — moving data around

# Reshape — change dimensions without changing data
arr = np.arange(12)          # [0,1,2,3,4,5,6,7,8,9,10,11]
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns — same 12 elements
print(matrix)

# -1 means "figure it out automatically"
auto = arr.reshape(4, -1)    # 4 rows, NumPy calculates columns = 3
print(auto)

# Flatten — collapse any shape back to 1D
flat = matrix.flatten()
print(flat)

# Stack arrays together — used when combining datasets
# change dimension just to see what happen
a = np.array([[1, 2, 3], [7, 8, 9]])
b = np.array([[4, 5, 6], [11, 12, 13]])

horizontal = np.hstack([a, b])  # [1,2,3,4,5,6]
vertical   = np.vstack([a, b])  # [[1,2,3],[4,5,6]]
print(horizontal)
print(vertical)
print(vertical.shape)           # (2,3) — 2 rows, 3 columns


# Mini project — Student marks analyser with NumPy 
# Build a complete marks analysis system — no Python loops allowed
import numpy as np

# 30 students, 5 subjects each — random data
np.random.seed(42)   # seed makes random repeatable — same numbers every run
marks = np.random.randint(40, 100, size=(30, 5))
# shape (30, 5) — 30 students, 5 subjects

subjects = ["Maths", "Python", "Physics", "English", "Science"]

# Answer all 8 questions using NumPy — NO for loops anywhere
# Every answer must be one or two lines of NumPy code

# 1. What is each student's total marks? (30 values)
total_of_each_student = marks.sum(axis=1)
print("Marks of each student : ", total_of_each_student)

# 2. What is each student's average marks? (30 values)
avg_of_each_student = marks.mean(axis=1)
print("Average marks of each student : ", avg_of_each_student)

# 3. What is the class average for each subject? (5 values)
class_avg_of_each_subject = marks.mean(axis=0)
print("Average of class for each Subject : ", class_avg_of_each_subject)

# 4. Which subject has the highest class average?
#    print the subject name, not just the index
maximum_avg_subject = np.argmax(class_avg_of_each_subject)
print(subjects[maximum_avg_subject], "has maximum average")


# 5. How many students scored above 75 in Python (subject index 1)?
students_scores_above = np.sum(marks[ : , 1] > 75, axis=0)
print(students_scores_above, "Students score above 75 in ", subjects[1])

# 6. Who is the top student? (highest total marks)
#    print their index and their total
top_student = np.argmax(total_of_each_student)
print(f"Top student is at position : {top_student} with {marks[top_student].sum()}")

# 7. Normalise the marks for Maths (subject index 0)
#    using Z-score: (value - mean) / std
#    print the first 5 normalised values
mean = marks[ : ,0].mean(axis = 0)
std = marks[ : , 0].std(axis = 0)
Z_score = (marks[ : ,0] - mean) / std
print("first 5 normalized values : ", Z_score[ : 5])

# 8. Create a pass/fail array — True if student average >= 60, False if not
#    How many students passed?
pass_fail = avg_of_each_student > 60
pass_students = np.sum(pass_fail == True)
print(pass_fail)
print(pass_students)

print("Shape of marks array:", marks.shape)
print("Subjects:", subjects)
