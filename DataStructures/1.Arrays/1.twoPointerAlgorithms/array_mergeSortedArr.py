class MergeSortedArray:

    def __init__(self) -> None:
        pass

    def mergeSortedArray(self, arr1, arr2):

        p1 = 0
        p2 = 0

        result = []

        while p1 < len(arr1) and p2 < len(arr2):

            if arr1[p1] < arr2[p2]:
                result.append(arr1[p1])

                p1 += 1

            elif arr1[p1] > arr2[p2]:

                result.append(arr2[p2])

                p2 += 1

        while p1 < len(arr1):
            result.append(arr1[p1])
            p1 += 1

        while p2 < len(arr2):
            result.append(arr2[p2])
            p2 += 1

        return result


obj = MergeSortedArray()

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]

ans = obj.mergeSortedArray(arr1, arr2)

print(ans)
