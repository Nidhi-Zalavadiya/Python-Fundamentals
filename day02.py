#Task 1 — loops
#A for loop + range — 5 programs, write all from scratch
# 
# # 1. Print numbers 1 to 10
# print(n for n in range(1,11))
print('Print numbers 1 to 10')
for i in range(1,11):
    print(i,sep=" ")

# 2. Print only even numbers from 1 to 20
print('print only even numbers from 1 to 20')

for i in range(1,21):
    if i % 2 == 0:
        print(i)
# print(n for n in range(1,21) if n % 2 == 0 )

# 3. Print multiplication table of 7 (7x1 to 7x10)
print('multiplication table of 7 (7x1 to 7x10)')
for i in range(10):
    print(f'7X{i+1}={7*(i+1)}')
# 4. Sum all numbers from 1 to 100 using a loop
print('Sum all numbers from 1 to 100 using a loop')
sumOfNumber = 0
for i in range(100):
    sumOfNumber = sumOfNumber + (i+1)
print(sumOfNumber)
# 5. Count how many times "a" appears in this string:
sentence = "a python developer who loves data and ai"
print('Count how many times "a" appears in this string: ',sentence ,"a Appear ", sentence.count('a'),"Times")
c = 0
for i in sentence:
    if i == "a":
        c += 1
print(c)

#B while loop — write these 3

# 1. Print numbers 1 to 5 using while loop
print('Print numbers 1 to 5 using while loop')
i = 1
while i <= 5:
    print(i)
    i = i+1
# 2. Keep asking user for a password until they type "python123".
#    use input() and a while loop
#    print "Access granted" when correct
print('Keep asking user for a password until they type "python123"')
while 1:
    p = input("Enter Password : ").lower().split()
    # p.lower()  Strings in Python are immutable. .lower() returns a new string — it does not modify p in place. You must reassign.
    # p.strip()
    if p == "python123":
        print("Access granted")
        break

# 3. Find the first number greater than 100
#    that is divisible by both 7 and 3
#    use while loop with break
num = 101
while True:
    if num % 7 == 0 and num % 3 == 0:
        print(num,' is first greater than 100 which is divisible by both 7 and 3')
        break
    num += 1



#C Loop + list together — this is interview level

numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]

# 1. Print only numbers greater than 5
print('Print only numbers greater than 5')
print([n for n in numbers if n > 5])

# 2. Create a new list with each number squared
#    do this WITH a for loop first
#    then do the SAME thing with a list comprehension (1 line)
print('Create a new list with each number squared WITH a for loop')
squered_list = []
for i in numbers:
    squered_list.append(i**i)
print(squered_list)
squered_list2 = [n**n for n in numbers]
print('list comprehension ', squered_list2)

# 3. Separate the list into two lists:
#    evens = [all even numbers]
#    odds  = [all odd numbers]
even = [n for n in numbers if n % 2 == 0]
print('Even List',even)
odd = [n for n in numbers if n % 2 != 0]
print('Odd List',odd)

# 4. Find the second largest number
#    without using sort() or max()
#    write the logic yourself
max = numbers[0]
sec_max = numbers[1]
for i in numbers:
    if i > max:
        sec_max = max
        max = i
    elif i > sec_max and i < max:
        sec_max = i
print("Second Max number in ",numbers," is ",sec_max)


#Task 2 — string methods
#A Basic string operations — write all 8

name = "  nidhi patel  "
email = "nidhi.patel@gmail.com"
sentence = "python is the best language for ai and ml"

# 1. Remove spaces from name and make it uppercase
print('Remove spaces from name and make it uppercase ', name)
print(name.strip().upper())

# 2. Check if email ends with ".com" — print True/False
print("Is Email endswith .com ? ", email.endswith(".com"))

# 3. Replace "best" with "top" in sentence
print('Replace "best" with "top" in',sentence)
s = sentence.replace("best","top")
print(s)

# 4. Split sentence into a list of words
print('Split sentence into a list of words')
l = sentence.split()
print(l)
# 5. Count how many words are in the sentence
print('Count how many words are in the sentence')
print(len(sentence.split()))

# 6. Capitalize the first letter of each word in sentence
print(sentence.title())
# 7. Check if "python" is in sentence — print True/False
print(True if "python" in sentence else False)

# 8. Extract only the username from email
#    (the part before @) — do not hardcode it
print(email.split("@")[0])



#B String + loop together — think before coding

words = ["mango", "apple", "banana", "avocado", "blueberry", "apricot"]

# 1. Print all words that start with "a"
n = [w for w in words if w.startswith("a")]
print(n)

# 2. Print all words longer than 5 characters
n = [w for w in words if len(w) > 5]
print(n)

# 3. Create a new list: all words in UPPERCASE
#    use list comprehension — 1 line only
upper_list = [u.upper() for u in words]
print(upper_list)

# 4. Join all words into one string separated by " | "
#    output: "mango | apple | banana | ..."
print(" | ".join(words))



#Mini project 
#Word analyzer — build this complete program

text = """Python is a powerful language. Python is used in
web development, data science, and artificial intelligence.
Many developers love Python because Python is simple."""

# Build these 6 things using only loops and string methods:
# 1. Count total number of words
print(len(text.split()))
# 2. Count how many times "Python" appears (case-insensitive)
print(text.count("Python"))


# 3. Find the longest word in the text
l = set(text.split())
large = {n:len(n) for n in l}
max,s = 0,""
for k,v in large.items():
    if v > max:
        s,max = k,v
print(s," is the Largest word in text with ",max, " letters")

# 4. Print all unique words (no duplicates) — use a set
print('Print all unique words')
n = set(text.split())
print(n)

# 5. Count total number of sentences (hint: split by ".")
print('Count total number of sentences')
print(len(text.split(".")))

# 6. Print the 3 most repeated words and their count
#    (no Counter import — write the logic yourself using a dict)
print('Print the 3 most repeated words and their count')
l = text.split()
s = set(text.split())
d = {w:l.count(w) for w in s}
f,s,t = 0,0,0
fv,sv,tv = "","",""
# max = a for k,a in d.items() 
for k,v in d.items():
    if v < s and v > t:
        tv,t = k,v
    elif v < f and v > s:
        tv,t = sv,s
        sv,s = k,v
    elif v > f:
        tv,t = sv,s
        sv,s = fv,f
        fv,f = k,v
        
     
print(f'{fv} : {f} - > {sv} : {s} -> {tv} : {t}')

#Second method
sorted_words = sorted(d.items(), key=lambda x: x[1], reverse=True)
top3 = sorted_words[:3]
print(top3)

'''
Today's Chalange was little bit hard but i like to solve these complex problem
we can not say this to complex but yeah it was fun
last project was little bit hard it takes time to solve the probelm but yeah i did it
'''
