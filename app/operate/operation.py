class Operation:
    def __init__(self, first, second):
        self.first = float(first)
        self.second = float(second)

    def plus(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            return None
        return self.first / self.second
