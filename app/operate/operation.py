class Operation:
    def __init__(self, first, second):
        self.first = first
        self.second = second

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
