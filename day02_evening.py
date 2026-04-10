#A Generator vs list — understand the difference by doing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Run each line and write what it prints in a comment
gen = (n for n in numbers if n > 5)
lst = [n for n in numbers if n > 5]

#This will print generator something like <generator...> 
print(gen)   # what does this print? why?
#This will print list like [6,7,8,9,10] Bcz We perform list comprehension here
print(lst)   # what does this print? why?

# Now iterate the generator with a for loop
for item in gen:
    print(item)

# Try to iterate it again — what happens? why?
for item in gen:
    print(item) 
# I don't know why nothing is printed here...
# surprising result — write why in a comment


#B String immutability — 5 exercises, predict output first
word = "  Hello World  "

# Predict output BEFORE running. Write prediction in comment.
# Then run and check.

result1 = word.strip()
print(word)   # changed or not? Won't Change bcz strings are immutable we can not change string it self instead crate new string with modification
print(result1) # what is this? this is new sting 

result2 = word.strip().lower().replace("world", "python")
print(result2) # what is this? This is new modified string in which from word string it replace value and make character lower plus strip the spaces

# Now fix these broken lines — each has the immutability bug
name = "nidhi"
name = name.upper()                     # bug: fix this
print(name)                      # should print NIDHI

sentence = "  python is great  "
sentence = sentence.strip()                 # bug: fix this
sentence = sentence.replace("great","best") # bug: fix this
print(sentence)                  # should print "python is best"


#C Power operator and math — 6 quick problems

# Write the output as a comment, then run to verify
print(2 ** 10)   # ? 1024
print(9 ** 0.5)  # ? (hint: square root) 3
print(3 ** 3)    # ? 27

# Write functions for these:
def square(n):
    # return n squared using **
    return n ** 2

def cube(n):
    # return n cubed
    return n ** 3

def power(base, exp):
    # return base to the power of exp
    return base ** exp

# Test:
print(square(5))    # 25
print(cube(3))      # 27
print(power(2, 8))  # 256


#D Rewrite this bad code with proper naming and style

# This is YOUR code from today — rewrite it with correct naming,
# spacing, and no single-letter variables

text = """Python is a powerful language. Python is used in
web development, data science, and artificial intelligence.
Many developers love Python because Python is simple."""

# Original (bad style):
# l = set(text.split())
# large = {n:len(n) for n in l}
# max,s = 0,""
# for k,v in large.items():
#     if v > max:
#         s,max = k,v
# print(s," is the Largest word in text with ",max, " letters")

# Your job: rewrite the same logic with:
# - descriptive variable names
# - proper spacing around : and ,
# - no shadowing of built-in max
# - clean f-string for the final print

text_set = set(text.split())
len_dictionary = {word : len(word) for word in text_set}

large_lenght, big_word = 0, ""

for word, lenght in len_dictionary.items():
    if lenght > large_lenght:
        big_word, large_lenght = word, lenght

print(f'{big_word} is the largest word in text with {large_lenght} latters')