class SlidingWindow_maxAvg(object):

    def __init__(self):
        pass

    def maxSubArrayAvg(self, nums, k):

        def subAverage(sub, k):

            cSum = 0
            for i in range(len(sub)):
                cSum += sub[i]

            avg = cSum / k
            return avg

        # left pointer
        l = 0

        # averages list
        avgLs = []

        for r in range(len(nums)):

            currSub = nums[r: r+k+1]

            currAv = subAverage(currSub)

            avgLs.append(currAv)


nums = [1, 12, -5, -6, 50, 3]


ob = SlidingWindow_maxAvg()
res = ob.maxSubArrayAvg(nums, 4)

print(res)
