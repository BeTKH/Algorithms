def checkIfPalindrome(str_):

	left = 0
	right = len(str_)-1

	while (left < right):

		if str_[left] != str_[right]:
			return False
		left 	+=1
		right 	-=1
	return True


newString1 = "racecar"
newString2 = "aceba"

print("is 'racecar' palindrome ?",checkIfPalindrome(newString1))
print("is 'aceba' palindrome ?",checkIfPalindrome(newString2))
