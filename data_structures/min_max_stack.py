class MinMaxStack:
    def __init__(self):
        self.stack = list()
        self.min = []
        self.max = []

    def push(self, value):
        self.stack.append(value)

        if not len(self.min) and not len(self.max):
            self.min.append(value)
            self.max.append(value)
        else:
            min_value = self.min[-1]
            max_value = self.max[-1]
            self.min.append(min(value, min_value))
            self.max.append(max(value, max_value))

    def get_max(self):
        return self.max[-1]

    def get_min(self):
        return self.min[-1]

    def peek(self):
        return self.stack[-1] if self.stack else None

    def pop(self):
        val = self.stack.pop(-1)
        self.min.pop(-1)
        self.max.pop(-1)
        return val

if __name__ == '__main__':
    stack = MinMaxStack()
    for val in [10, -1, 5, 3, 100, -10]:
        stack.push(val)

    print(stack.get_max())
    print(stack.get_min())
    print(stack.stack)
    stack.pop()

    print(stack.get_max())
    print(stack.get_min())





