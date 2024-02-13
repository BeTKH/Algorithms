class Palindrome:

    def __init__(self):
        pass

    def isPalindrome(self, s):
        L = 0
        R = len(s) - 1
        while L < R:

            if s[L] != s[R]:

                return False
            else:
                L += 1
                R -= 1
            return True


obj = Palindrome()

word = "racecar"

result = obj.isPalindrome(word)

print(result)
