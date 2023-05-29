"""

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
 

Constraints:

s.length == indices.length == n
1 <= n <= 100
s consists of only lowercase English letters.
0 <= indices[i] < n
All values of indices are unique.

"""

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """

    str_lst = list(s)

    for i, s in zip(indices, list(s)):
        str_lst[i] = s

    return "".join(str_lst)

s1 = "codeleet"
indices1 = [4,5,6,7,0,2,1,3]


s2 = "abc"
indices2 = [0,1,2]

print(restoreString(s1, indices1))
print(restoreString(s2, indices2))