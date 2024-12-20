class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def isPalindorme(self, w):

            w = list(w)
            # left and right pointers L & R
            L = 0
            R = len(w) - 1

            while L < R:
                if w[L] != w[R]:
                    return False
                elif w[L] == w[R]:

                    L += 1
                    R -= 1
            return True

        # loop hrough each word, if palindrime return it else pass it
        for W in words:
            if isPalindorme(self, W):
                return W
            else:
                pass
        return ""


ob = Solution()

words = ["abc", "car", "ada", "racecar", "cool"]

f = ob.firstPalindrome(words)
print(f)
