#Algorithm for a Palindrome
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str)-1

    for x in str:
        if str[startIndex+1] != str[endIndex-1]:
            return False
    return True

print(isPalindrome('racecar'))