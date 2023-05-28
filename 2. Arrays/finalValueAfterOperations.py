"""
Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
Example 2:

Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
Example 3:

Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.

"""




def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    
    #X = 0
    
    ans = "".join(operations)
    
    result = ans.count("++") - ans.count("--")
    
    return result


def finalValueAfterOperations_2(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    
    # init x
    x = 0
    
    for i in operations:
        
        if i == "--X": 
            x = x-1
            
        elif i =="X--":
            x = x-1
            
        elif i =="++X": 
            x = x+1
        else:           
            x = x+1
            
    return x





operations_1 = ["--X","X++","X++"]
operations_2 = ["++X","++X","X++"]
operations_3 = ["X++","++X","--X","X--"]



print(finalValueAfterOperations(operations_1))
print(finalValueAfterOperations(operations_2))
print(finalValueAfterOperations(operations_3))