"""
Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
 

Constraints:

1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
sentences[i] consists only of lowercase English letters and ' ' only.
sentences[i] does not have leading or trailing spaces.
All the words in sentences[i] are separated by a single space.

"""


def mostWordsFound(sent):
    
    countwords = 0
    
    for s in sent:
        
        words = s.split()
        
        #clean trainling space and lowercase it
        words_clean = [w.lower().strip(" ") for w in words]
        
        
        # find max number of words
        if len(words_clean) > countwords:
            countwords = len(words_clean)
                
    return countwords


# fastest solution ( not necessarily good solution)

def mostWordsFound2(sentences):
    maximum = 0
    for a in sentences:
        b = a.count(" ")
        b += 1
        if b > maximum:
            maximum = b
    return maximum
        
    

sentence1 = ["alice and bob love leetcode ", "i think so too", "this is great thanks very much"]
sentence2 = ["please wait", "continue to fight", "continue to win"]


print(mostWordsFound(sentence1))
print(mostWordsFound(sentence2))