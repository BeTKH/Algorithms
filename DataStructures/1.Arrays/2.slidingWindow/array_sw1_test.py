"""
find the length of the longest subarray that 
has a sum less than or equal to k. 

For this example, let nums = [3, 2, 1, 3, 1, 1] 
and k = 5.



solution: slinding window
"""


class SubArray(object):

    def __init__(self):
        pass

    def longestSubArray(self, nums, k):

        # left pointer
        l = 0
        lenList = []

        # right pointer with for loop
        for r in range(len(nums)):

            # substring
            s = nums[l:r+1]

            currSum = sum(s)

            if currSum <= k:
                lenList.append(len(s))

            elif currSum > k:
                l += 1

        return max(lenList)


ob = SubArray()


k = 5
A = [3, 2, 1, 3, 1, 1]
result = ob.longestSubArray(A, k)

print(result)


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k2 = 8

res2 = ob.longestSubArray(nums, k2)
print(res2)
