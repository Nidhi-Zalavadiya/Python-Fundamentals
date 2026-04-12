# Mini project — Student records file system 

# Build a complete save/load system for student data
"""
Build these 4 functions — combine File I/O + Exceptions + your
Student class from Day 3 together for the first time
"""

def save_students(students, filename="students.txt"):
    """Save list of Student objects to a file — one per line
    Format: "Raj,21,85,90,78"  (name,age,mark1,mark2,mark3)
    Handle: IOError if file cannot be written
    """
    try:
        with open(f"Student Management System/{filename}", 'w') as f:
            for i in students:
                f.write(f"{i.name},{i.age},{','.join(map(str, i.marks))} \n")
    except IOError:
        raise IOError("File Cannot be written")
    else:
        print("Students Data Saved To the file")

def load_students(filename="students.txt"):
    """Load students from file — return list of Student objects
    Handle: FileNotFoundError if file does not exist
    Handle: ValueError if a line is badly formatted
    Skip corrupted lines — do not crash
    """
    try:
        with open(f"Student Management System/{filename}", 'r') as f:
            student_list = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("File May not Be exist")
    except Exception as e:
        print("Some thing went wrong", e)
    else:
        # This one was working correctly but not radable
        # list_of_students = [students_list.strip().split(',') for students_list in student_list]
        # loaded_list = [Student(student[0],student[1],[int(mark) for mark in student[2:]]) for student in list_of_students]
        # return loaded_list
        #This is readable
        loaded_list = []
        for line in student_list:
            try:
                parts = line.strip().split(',')
                student = Student(parts[0], parts[1], [int(m) for m in parts[2:]])
                loaded_list.append(student)
            except (ValueError, IndexError):
                print(f"Skipping corrupted line: {line.strip()}")
        return loaded_list
        # return Student(loaded_list)

def add_student(filename, name, age, marks):
    """Add one new student to existing file without overwriting
    Handle: all errors gracefully
    """
    try:
        with open(f"Student Management System/{filename}", 'a') as f:
            f.write(f"{name},{age},{','.join(map(str, marks))}")
    except IOError:
        raise IOError("can not write in file ", filename)
    except ValueError:
        raise ValueError("File format does not match")
    except Exception as e:
        print("Something went wrong", e)
    else:
        print(f"Student {name} Added Successfully")

def find_student(filename, name):
    """Search for a student by name — return Student object or None
    Case-insensitive search
    """
    try:
        with open(f"Student Management System/{filename}", 'r') as f:
            students_l = f.readlines()
            list_of_students = [students_list.strip().split(',') for students_list in students_l]
            for student in list_of_students:
                if name == student[0].strip().lower():                  
                    return Student(student[0],student[1],[int(mark) for mark in student[2:]])
            
    except Exception as e:
        print(e)

# Test the full system:
from day03_morning import Student

students = [
    Student("Raj", 21, [85, 90, 78]),
    Student("Priya", 22, [92, 88, 95]),
    Student("Amit", 20, [70, 65, 80]),
]

save_students(students)
loaded = load_students()
for s in loaded:
    print(s.introduce())

add_student("students.txt", "Nidhi", 21, [88, 92, 79])
found = find_student("students.txt", "nidhi")
if found:
    print(found.introduce())
