class TargetSum:

    def __init__(self):
        pass

    def sumTargetExisits(slef, arr, t):

        L = 0
        R = len(arr) - 1

        while L < R:

            sum_ = arr[L] + arr[R]

            if sum_ == t:
                return True, [L, R]
            elif sum_ < t:
                L += 1
            elif sum_ > t:
                R -= 1

        return False


obj = TargetSum()

ls = [1, 2, 4, 6, 8, 9, 14, 16]
t = 13

result = obj.sumTargetExisits(ls, t)

print(result)

