print(type(10)) #Int
print(type(10.5)) #float
print(type("hello")) #str
print(type(True)) #bool
print(type([1,2,3])) #list
print(type({"a":1})) #dict
print(type((1,2))) #tuple
print(type({1,2,3})) #set


#Task 1 : Data Structures

# A  : List operations — do all 6, no copy paste
fruits = ["mango", "banana", "apple"]
print("Raw List : ",fruits)
#Add grapes to the end
fruits.append("grapes")
print('Add grapes to the end ',fruits)
#insert "orange" at position 1
fruits.insert(0,"orange")
print('insert "orange" at position 1  ',fruits)
# 3. Remove "banana"
fruits.remove("banana")
print('Remove "banana" ',fruits)
# 4. Sort the list alphabetically
fruits.sort()
print("Sort the list alphabetically ",fruits)
# 5. Print the last item using negative index
print("Print the last item using negative index : ",fruits[-1])
# 6. Print a slice: only first 2 items
print("Print a slice: only first 2 items ", fruits[:2])


# B :  build student record
student = {
    "name" : "Raj",
    "age" : 21,
    "marks" : [85, 90, 78, 92, 88] 
}
print("Row Dictionary : ", student)
# 1. Print the student name
print("Print the student name : ",student["name"])
# 2. Add a new key "city" with value "Junagadh"
student["city"] = "Junagadh"
print('Add a new key "city" with value "Junagadh" : ', student)
# 3. Calculate average of marks and print it
print('Calculate average of marks and print it : ',sum(student["marks"])/len(student["marks"]))
# 4. Print all keys, then all values
print('Print all keys : ',student.keys())
print('Print all values : ',student.items())
# 5. Check if "email" key exists, print True/False
print("Email Exist" if "email" in student else "Email is not exist")



# C The difference question — understand this deeply
a = [1, 2, 3] 
b = a #This is Same Object Just Give The Reference of Object A to Object B When CHnage Object B WIll also change object A
b.append(4)
print(a) #This will print 1,2,3,4

c = [1, 2, 3]
d = c.copy() #Here We Use The Copy Function What this will do is it will create new indipendent object which is copy of object c it is not same only their values are same but both have different referance
d.append(4)
print(c) #This will print 1, 2, 3



#Task 2: Functions (this is where most beginners are weak)

#1 Write these 4 functions from scratch — no looking up syntax
def greet(name):
    # return "Hello, {name}!" using f-string
    return (f'Hello, {name}')

def add_numbers(a, b):
    # return sum
    return a + b

def is_even(n):
    # return True if n is even, False if odd
    return True if n/2 == 0 else False

def find_max(numbers):
    # given a list, return the largest number
    # do NOT use the built-in max() function
    # write the logic yourself using a loop
    m = numbers[0]
    for i in numbers:
        if i > m:
            m = i
    
    return m

print(greet("Nidhi"))
print("Sum Of 5 and 6 : ",add_numbers(5,6))
print("9 is Even : ", is_even(5))
l = [5, 99, 14 , 65, 0]
print("Max from  ", l , " = ", find_max(l))


#2 Default arguments and multiple returns — write this exactly
def describe_person(name, age, city="Junagadh"):
    # return a string like:
    # "Raj is 21 years old from Junagadh"
    return (f'{name} is {age} years old from {city}')

def min_max(numbers):
    # return BOTH minimum AND maximum
    # call it like: low, high = min_max([3,1,4,1,5])
    # print both 
    low,high = min(numbers), max(numbers)
    return low, high

print("Person Description : ",describe_person("Nidhi",22))
print("Minimum And Maximum From [3,1,4,1,5] : ",min_max([3,1,4,1,5]))


#3 Mini project — combine everything into one program
students = [
    {"name": "Raj",   "marks": [85, 90, 78]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Amit",  "marks": [70, 65, 80]},
]

# Write a function: get_average(marks) -> returns average
def get_average(marks):
    return sum(marks)/len(marks)

# Write a function: get_grade(avg) -> returns "A","B","C","F"
def get_grade(avg):
    #   A = 90+, B = 75+, C = 60+, F = below 60
    if avg > 90:
        return "A"
    elif avg <=90 and avg > 75:
        return "B"
    elif avg <=75 and avg > 60:
        return "C"
    else:
        return "D"

# Loop through students, print:
#   "Raj: avg=84.3, grade=B"
#   "Priya: avg=91.7, grade=A"  
#   "Amit: avg=71.7, grade=C"
for student in students:
    avg = get_average(student["marks"])
    print(f'students[name]: avg={avg:.2f}, grade={get_grade(avg)}')

'''
Today I Learn About Datatypes and i was confuse in dictionary 
when add new item but i do not use google or any ai i just start thinking
why, where's the actul problem then i try some syntax and suddenly remember
how to insert new key value pair in dictionary it was really fun. 
this is warm up for me i remember all the fundaments 
when i start writing code it was fun and honestly i do not feel lazzy or bored
i love coding 
'''