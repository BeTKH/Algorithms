"""

working solution!!!!

"""


class SlidingWindow(object):

    def __init__(self):
        pass

    def longestSubstringOne(self, s):

        s = list(s)

        l = 0
        lenList = []

        for r in range(len(s)):

            # current substring
            currSub = s[l:r+1]

            # no of zeros in current sibstring
            countZ = currSub.count('0')

            if countZ <= 1:

                lenList.append(len(currSub))

            elif countZ > 1:
                l += 1

        return max(lenList)


s = "1101100111"
s2 = "11001011"

ob = SlidingWindow()

res = ob.longestSubstringOne(s)
res2 = ob.longestSubstringOne(s2)

print(res)
print(res2)
