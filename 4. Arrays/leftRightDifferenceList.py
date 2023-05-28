"""
Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

"""



def leftRightDifference(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    #initialize 
    lefSum = [0,]
    rigSum = [0,]
    difference = []

    #duplicate nums for use to find rightSum
    numsCopy = list(nums)
    
    
    for i in range(len(nums)):

        #codition - find sums until length(nums) -1, bcz we have initialized
        if i < len(nums)-1:

            #leftsum
            leftCurrent = nums[0:i+1]
            lefSum.append(sum(leftCurrent))


            #rightSum
            #delete the first element on each loop
            numsCopy.pop(0)

            #update rightCurrent
            rightCurrent = numsCopy

            #insert the right sum at the beginning of the rightSum 
            rigSum.insert(i, sum(rightCurrent))

            
        # finally find the difference 
        difference.append( abs(lefSum[i] - rigSum[i]))

        
    return difference
    

    
nums1 = [10,4,8,3]
nums2 = [1]


print(leftRightDifference(nums1))
print(leftRightDifference(nums2))