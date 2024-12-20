text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]

ans = []
for i in words:
	
	curr = []

	start = text.find(i)
	end = start + len(i)-1

	curr.append(start)
	curr.append(end)

	ans.append(curr)

print(ans)