class MergeSA:

    def __init__(self):
        pass

    def merger(self, A1, A2):

        p1 = p2 = 0

        res = []

        while p1 < len(A1) and p2 < len(A2):

            if A1[p1] < A2[p2]:
                res.append(A1[p1])
                p1 += 1

            elif A1[p1] > A2[p2]:
                res.append(A2[p2])
                p2 += 1

        while p1 < len(A1):
            res.append(A1[p1])
            p1 += 1

        while p2 < len(A2):
            res.append(A2[p2])
            p2 += 1

        return res


obj = MergeSA()

a1 = [3, 10]
a2 = [9, 11, 22, 28]

ans = obj.merger(a1, a2)

print(ans)
