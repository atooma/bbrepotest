class BBErrorException(Exception):
    pass

class BBRepoTest(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b