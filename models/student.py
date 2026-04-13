class Student:
        # __init__ takes: name, age, marks (list)
        # store all three as instance variables
        def __init__(self, name, age, marks):
            self.name = name
            self.age = age
            self.marks = marks

        def get_average(self):
            # calculate and return average of marks
            avg = sum(self.marks) / len(self.marks)
            return avg 

        def get_grade(self):
            # return "A", "B", "C", or "F"
            # A=90+, B=75+, C=60+, F=below 60
            avg = self.get_average()
            if avg > 90:
                return ("A")
            elif avg > 75 and avg <= 90:
                return ("B")
            elif avg > 60 and avg <= 75:
                return ("C")
            else:
                return ("F")

        def introduce(self):
            # return a string like:
            # "Hi, I am Raj, age 21, grade B"
            return (f'Hi, I am {self.name}, age {self.age}, grade {self.get_grade()}')

        def add_mark(self, mark):
            # add a new mark to self.marks
            self.marks.append(mark)

if __name__ == "__main__":
    # test code that only runs when you run student.py directly
    # not when it is imported by another file
    s = Student("Test", 20, [80, 90, 85])
    print(s.introduce())