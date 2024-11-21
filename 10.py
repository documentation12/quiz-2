# # 1
#
# def lyrics(lyrrics):
#     my_dict = {}
#     for word in lyrrics:
#         if word in my_dict:
#             my_dict[word] += 1
#         else:
#             my_dict[word] = 1
#     return my_dict
#
#
# lyr = ['hello', 'hello', 'world', 'world', 'world']
#
# print(lyrics(lyr))
#

#  better solution

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


# 2

# def most_common_words(freqs):
#     values = freqs.values()
#     best = max(values)
#     words = []
#     for k in freqs:
#         if freqs[k] == best:
#             words.append(k)
#     return words, best
#
#
# print(most_common_words({'a': 5, 'b': 5, 'c': 5, 'd': 5}))

# better solution

# def most_common_words(freqs):
#     best = max(freqs.values())
#     words = [k for k, v in freqs.items() if v == best]
#     return words, best
#
#
# print(most_common_words({'a': 5, 'b': 5, 'c': 5, 'd': 5}))
#
#
# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = most_common_words(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del (freqs[w])
#         else:
#             done = True
#     return result
#
#
# print(words_often({'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 2, 'f': 2, 'g': 2, 'h': 2}, 3))


# 3

# def how_many(aDict):
#     count = 0
#     for k in aDict:
#         count += len(aDict[k])
#     return count
#
#
# animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
#
# print(how_many(animals))
#
#
# #  better solution
#
# def how_many(aDict):
#     return sum(len(value) for value in aDict.values())
#
#
# animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
#
# print(how_many(animals))

#   4

def biggest(aDict):
    if len(aDict) == 0:
        return None
    else:
        return max(aDict, key=lambda x: len(aDict[x]))


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
