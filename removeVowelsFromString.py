



# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
#
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.
#


#test cases
testList = [
    ("a", ""),
    ("ab", "b"),
    ("g", "g"),
    ("aaaaab", "b"),
    ("bbbbba", "bbbbb"),
    ("abababa", "bbb")
]

# this problem requires us to modify a string and return it,but python strings are immutable
# a new string may be required for us to skip vowels
#if a char in a string is a vowel, skip it, else put it in the string we want to return
# to make things cleaner, a function that checks whether a char is a vowel is needed

#thoughts on time complexity:
#we must go through the entire array

def isVowel(c)->bool:

    vowels = ['a','e','i','o','u']

    if c in vowels:
        return True
    else:
        return False



def removeVowels(str1)->str:

    noVowels = ""
    for x in range(len(str1)):

        if isVowel(str1[x]):

            continue
        else:

            noVowels +=str1[x]

    return noVowels

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for (test_in, expected) in testList:
        result = removeVowels(test_in)
        result_str = "passed" if result == expected else "FAILED"
        print(result_str, ' test_in: ', test_in, ' result: ', result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


