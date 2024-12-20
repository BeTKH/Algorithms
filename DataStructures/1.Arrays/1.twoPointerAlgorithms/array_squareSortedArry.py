class SquareArray(object):

    def __init__(self):
        pass

    def sqrSortedArray(self, nums):

        L = 0
        R = len(nums) - 1

        res = [0] * len(nums)
        res_index = len(nums) - 1

        while L < R:

            leftProd = nums[L] * nums[L]
            rightProd = nums[R] * nums[R]

            if leftProd < rightProd:

                res[R] = rightProd
                res[R-1] = leftProd
                R -= 1
                L += 1

            elif leftProd > rightProd:

                res[R] = leftProd
                res[R-1] = rightProd

                R -= 1
                L += 1

            res_index -= 1

        return res


nums = [-4, -1, 0, 3, 10]

ob = SquareArray()
ans = ob.sqrSortedArray(nums)

print(ans)
