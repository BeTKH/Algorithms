class Substringer:

    def __init__(self):
        pass

    def isSubstring(self, t, s):

        p1 = p2 = 0
        res = []

        while p1 < len(t) and p2 < len(s):

            if t[p1] == s[p2]:

                res.append(t[p1])
                p1 += 1
                p2 += 1

            elif t[p1] != s[p2]:
                p1 += 1

        if res == list(s):
            return True


obj = Substringer()

T = "abcde"
S = "ace"

ans = obj.isSubstring(T, S)

print(ans)
