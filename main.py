import matplotlib as plt
import numpy as np

np.random.seed(0)

if __name__ == '__main__':
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.scatter(x, y)
    plt.show()

    