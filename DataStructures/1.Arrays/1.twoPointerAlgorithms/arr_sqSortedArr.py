class SqArr(object):

    def __init__(self):
        pass

    def sqSortedArray(self, A):

        L = 0
        R = len(A) - 1
        ind = len(A) - 1

        res = [0] * len(A)

        while L <= R:

            lProd = A[L] * A[L]
            rProd = A[R] * A[R]

            if lProd > rProd:
                res[ind] = lProd
                L += 1

            elif lProd < rProd:
                res[ind] = rProd
                R -= 1

            elif lProd == rProd:
                res[ind] = lProd
                L += 1

            ind -= 1

        return res


l = [-7, -3, 2, 3, 11]

ob = SqArr()

r = ob.sqSortedArray(l)

print(r)
