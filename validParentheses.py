


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.





# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



#first idea:
#if you have a data structure that pops matching brackets, a valid string would be empty at the end
#possible data structure to use:  stack
#push chars onto stack one at a time, as new chars are pushed, check if the current char to be pushed
#matches with char at the top of the stack
#if they match, pop the last char from the stack and do not add the char being compared to the char
#at the top of the stack
#if no match, add the new char to the stack
#if the string is empty at the end, the string is valid

#may need a function or two to check if two chars match





testCases = ["(",
             "[]",
             "[[]",
             "[{()}]",
             "{",
             "[{[{{"]


def isMatch(c1,c2)->bool:


    left = ["[","{","("]
    right = ["]","}",")"]

    if c1 in left and c2 in right:

        return True

    else:

        return False

def validParentheses(str1)-> bool:

    if len(str1) == 1:
        return False
    #use a list as a stack

    stack = []

    stack.append(str1[0])
    for i in range(1,len(str1)):

        if isMatch(stack[-1],str1[i]):

            stack.pop()

            continue
        else:
            stack.append(str1[i])


    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':


    for i in range(len(testCases)):
        print(validParentheses(testCases[i]))