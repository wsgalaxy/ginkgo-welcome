class other(object):
    i = 1
    def __init__(self):
        self.v = 10

class other2(other):
    def __init__(self, **kwargs):
        super().__init__()
        print(type(super))
        print(type(super()))
        s = super()
        print(self.v)


o = other2()
