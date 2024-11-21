# # 1
#
# from functools import reduce
#
#
# def add_random_numbers(dict1):
#     import random
#
#     for key in dict1:
#         if key == 'a':
#             dict1[key].append(random.randint(1, 10))
#         elif key == 'b':
#             dict1[key].extend(random.randint(1, 10) for _ in range(2))
#         elif key == 'c':
#             dict1[key].extend(random.randint(1, 10) for _ in range(4))
#
#     max_key = max(dict1, key=lambda k: len(dict1[k]))
#
#     all_values = []
#     for values in dict1.values():
#         for num in values:
#             all_values.append(num)
#
#     total_product = reduce(lambda x, y: x * y, all_values)
#
#     return max_key, total_product
#
#
# dict1 = {'a': [], 'b': [], 'c': []}
# max_key, total_product = add_random_numbers(dict1)
# print("Updated Dictionary:", dict1)
# print("Key with Maximum Length:", max_key)
# print("Product of All Values:", total_product)
#
#
# # 2
#
# from collections import Counter
#
#
# def lyrics(lyrrics):
#     return Counter(lyrrics)
#
#
# lyr = ['hello', 'hello', 'world', 'world', 'world']
#
# print(lyrics(lyr))

# 3
# import random
#
#
# def sia(length, start=0, end=100):
#     lst = []
#     for i in range(length):
#         lst.append(random.randint(start, end))
#
#     return lst
#
#
# try:
#     length = int(input("Enter the length of the list: "))
#     start = int(input("Enter the start of the range: "))
#     end = int(input("Enter the end of the range: "))
#     print(sia(length, start, end))
# except ValueError:
#     print("Invalid Input")

# 4

# import os
# import random
#
#
# def create_txt_file():
#     desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#     file_name = os.path.join(desktop, 'random_numbers.txt')
#
#     with open(file_name, 'w') as file:
#         for _ in range(10):
#             file.write(str(random.randint(1, 100)) + '\n')
#
#
# create_txt_file()


# 5


names = ['John', 'Paul', 'George', 'Ringo']
grades = ["A", "B", "C", "D"]
scores = [2.0, 3.0, 4.0, 1.0]


def make_student_dict(name, names, grades, scores):
    student_dict = {}

    for i in range(len(names)):
        student_dict[names[i].lower()] = {'name': names[i], 'grade': grades[i], 'score': scores[i]}

    if name in student_dict:
        return student_dict[name]

    return "ჩანაწერი არ არსებობს"


name = input("Enter the name of the student: ").lower()
print(make_student_dict(name, names, grades, scores))
