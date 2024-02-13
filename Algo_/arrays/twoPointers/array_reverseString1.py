class RevStr(object):

    def __init__(self):
        pass

    def revStr(self, str_):

        str_ = list(str_)

        p1 = 0
        p2 = len(str_) - 1

        while p1 < p2:

            str_[p1], str_[p2] = str_[p2], str_[p1]

            p1 += 1
            p2 -= 1

        return str_


s = "1234"

obj = RevStr()

res = obj.revStr(s)

print(res)
