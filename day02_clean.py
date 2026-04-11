#Mini project 
#Word analyzer — build this complete program

text = """Python is a powerful language. Python is used in
web development, data science, and artificial intelligence.
Many developers love Python because Python is simple."""

# Build these 6 things using only loops and string methods:
# 1. Count total number of words
print('Count total number of words in ', text)
print(len(text.split()))
# 2. Count how many times "Python" appears (case-insensitive)
print('Count how many times "Python" appears in ',text)
print(text.count("Python"))


# 3. Find the longest word in the text
text_set = set(text.split())
len_dictionary = {word : len(word) for word in text_set}

large_length, big_word = 0, ""

for word, length in len_dictionary.items():
    if length > large_length:
        big_word, large_length = word, length

print(f'{big_word} is the largest word in text with {large_length} letters')

# 4. Print all unique words (no duplicates) — use a set
print('Print all unique words')
unique_value = set(text.split())
print(unique_value)

# 5. Count total number of sentences (hint: split by ".")
print('Count total number of sentences')
print(len(text.split(".")))

# 6. Print the 3 most repeated words and their count
#    (no Counter import — write the logic yourself using a dict)
print('Print the 3 most repeated words and their count')

text_list = text.split()
unique_words = set(text.split())
count_dict = {w : text_list.count(w) for w in unique_words}

first_count, second_count, third_count = 0, 0, 0
first_value, second_value, third_value = "", "", ""

for word, count in count_dict.items():
    if count > first_count:
        third_value, third_count = second_value, second_count
        second_value, second_count = first_value, first_count
        first_value, first_count = word, count
    elif count > second_count:
        third_value, third_count = second_value, second_count
        second_value, second_count = word, count
    elif count > third_count:
        third_value, third_count = word, count
    
print(f'{first_value} : {first_count} -> {second_value} : {second_count} -> {third_value} : {third_count}')

#Second method
sorted_words = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
top3 = sorted_words[:3]
print(top3)

'''
Today's Chalange was little bit hard but i like to solve these complex problem
we can not say this to complex but yeah it was fun
last project was little bit hard it takes time to solve the probelm but yeah i did it
'''
