class ReverseStr:

    def __init__(self):
        pass

    def revStr(self, s):

        s = list(s)
        # points to the end of the string/list
        p = len(s) - 1

        # store reversed str
        resvStr = []
        while p >= 0:

            resvStr.append(s[p])

            p -= 1

        return "".join(resvStr)


obj = ReverseStr()

s = "Hello"

ans = obj.revStr(s)

print(ans)
