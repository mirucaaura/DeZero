import numpy as np


class Variable:
    def __init__(self, data) -> None:
        self.data = data


data = np.array(1.0)
x = Variable(data)
print(x.data)
