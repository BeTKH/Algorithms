class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        ans = []
        for r in range(len(nums)):

            sub = nums[r: r+k]
            sum_ = float(sum(sub))
            av = (sum_/float(k))
            ans.append(av)

            if r + k > len(nums):
                break

        return max(ans)


ob = Solution()


nums = [1, 12, -5, -6, 50, 3]

ans = ob.findMaxAverage(nums, 4)
print(ans)
