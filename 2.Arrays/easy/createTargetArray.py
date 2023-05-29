"""
Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]

"""

def createTargetArray(nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
        
    target = []
    for i, n in zip(index, nums):
        target.insert(i, n)
    return target



nums1 = [0,1,2,3,4]
index1 = [0,1,2,2,1]

nums2 = [1,2,3,4,0]
index2 = [0,1,2,3,0]

nums3 = [1]
index3 = [0]


print(createTargetArray(nums1, index1))
print(createTargetArray(nums2, index2))
print(createTargetArray(nums3, index3))