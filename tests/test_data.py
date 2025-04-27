from pywhiten2.data import *
import pywhiten2.optimization
import numpy as np

def test_frequency():
    x = np.linspace(0, 100, 1000)
    testFreq = Frequency(1.2, 3.2, 0.2)
    y = testFreq.evaluate(x)
