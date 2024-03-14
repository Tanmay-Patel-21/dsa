# Problem statement
# You have been given an array/list of strings 'inputStr'. You are supposed to return the strings as groups of anagrams such that strings belonging to a particular group are anagrams of one another.

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. We can generalize this in string processing by saying that an anagram of a string is another string with the same quantity of each character in it, in any order.

# Note:
# The order in which the groups and members of the groups are printed does not matter.
# For example:
# inputStr = {"eat","tea","tan","ate","nat","bat"}
# Here {“tea”, “ate”,” eat”} and {“nat”, “tan”} are grouped as anagrams. Since there is no such string in “inputStr” which can be an anagram of “bat”, thus, “bat” will be the only member in its group.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1<= T <= 50
# 1<= N <= 100
# 1<= K <= 10

# Where 'T' is the number of test cases, 'N' is the length of the given array/list of strings and ‘K’ is the maximum length of a string in the given array/list.

# Time limit: 1 sec.
# Sample Input 1:
# 2
# 4
# abab baba aabb abbc
# 5
# aecd bcda acbd abdc acda
# Sample Output 1 :
# aabb abab baba
# abbc
# abdc acbd bcda
# acda
# aecd
# Explanation of the Sample Input 1 :
# In the first test case, in the first group ["aabb", "abab", "baba"], all the strings are anagrams of one another and in the second group ["abbc"] has no anagram, so it's the only member in its group.

# In the second test case, in the first group ["abdc", "acbd", "bcda"] all the strings are anagrams of one another, and in second and third group, both ["acda"] and ["aecd"] have no anagram, so they are the only member in their group
# Sample Input 2:
# 2
# 6
# eat tea tan ate nat bat
# 5
# cat dog tac god act
# Sample Output 2 :
# ate eat tea
# bat
# nat tan
# act cat tac
# dog god
# Explanation of the Sample Input 2 :
# In the first test case, in the first group ["ate", "eat", "tea"] and the third group [“nat”, “tan”], all the strings are anagrams of one another and in the second group ["bat"] has no anagram, so it's the only member in its group and,

# In the second test case, in the first group ["act", "cat", "tac"] and in the second group ["dog", "god"], all the strings are anagrams of one another.
# Python (3.5)
# 1234567891011121314151617181920212223242526272829303132
# from os import *
# from sys import *
# from collections import *
# from math import *

# from sys import stdin, setrecursionlimit
# setrecursionlimit(10**7)


# def getGroupedAnagrams(inputStr):

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getGroupedAnagrams(inputStr):
    myMap = {}

    for i in inputStr:
        key = ''.join(sorted(i))
        if key in myMap.keys():
            myMap[key].append(i)
        else:
            myMap[key] = [i]

    return [value for value in myMap.values()]


def takeInput():
    n = stdin.readline().strip()
    inputStr = list(stdin.readline().strip().split(" "))
    return inputStr, n


def printAnswer(groupedAnagram):
    for group in groupedAnagram:
        group.sort()

    groupedAnagram.sort()
    print('\n'.join(map(' '.join, groupedAnagram)))


T = int(stdin.readline().strip())

for i in range(T):
    inputStr, n = takeInput()
    groupedAnagram = getGroupedAnagrams(inputStr)
    printAnswer(groupedAnagram)
