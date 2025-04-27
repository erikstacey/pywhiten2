import numpy as np


def sinusoidal(x, frequency, amplitude, phase):
    return amplitude * np.sin((2*np.pi * (frequency * x + phase)))