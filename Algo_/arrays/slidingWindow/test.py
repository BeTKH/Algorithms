# def find_length(nums, k):
#     # curr is the current sum of the window
#     left = curr = ans = 0
#     for right in range(len(nums)):
#         curr += nums[right]
#         while curr > k:
#             curr -= nums[left]
#             left += 1
#         ans = max(ans, right - left + 1)

#     return ans


# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
# k2 = 8


# ans = find_length(nums, k2)
# print(ans)


nums = [10, 5, 2]


def arryProd(nums):

    curr = 1
    for i in range(len(nums)):
        curr = curr * nums[i]

    return curr


a = arryProd(nums)

print(a)
