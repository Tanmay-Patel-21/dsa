# Problem statement
# You have been given two strings 'STR1' and 'STR2'. You have to check whether the two strings are anagram to each other or not.

# Note:
# Two strings are said to be anagram if they contain the same characters, irrespective of the order of the characters.
# Example :
# If 'STR1' = “listen” and 'STR2' = “silent” then the output will be 1.

# Both the strings contain the same set of characters.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= |STR1|, |STR2| <= 10^3

# Where |STR1| and |STR2| are the lengths of the string 'STR1' and 'STR2' respectively.

# Time limit: 1 sec
# Sample Input 1:
# 2
# listen silent
# east eats
# Sample Output 1:
# 1
# 1
# Explanation for Sample Output 1:
# In test case 1, "listen" and "silent" has same set of characters.

# In test case 2, "east" and "eats" has same set of characters.
# Sample Input 2:
# 2
# triangle integral
# hearts earth
# Sample Output 2:
# 1
# 0
# Explanation for Sample Output 1:
# In test case 1, "triangle" and "integral" has same set of characters.

# In test case 2, "hearts" and "earth" does not have same set of characters.
from os import *
from sys import *
from collections import *
from math import *


def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return 0
    count = {}
    for i in range(len(str1)):
        if (str1[i] in count):
            count[str1[i]] += 1
        else:
            count[str1[i]] = 1
    for i in range(len(str2)):
        if (str2[i] in count):
            count[str1[i]] -= 1

    for key in count.keys():
        if (count[key] != 0):
            return 0

    return 1
