import numpy as np
from typing import Callable
from dataclasses import dataclass
from pywhiten2.optimization.models import sinusoidal

@dataclass
class Frequency:
    """ Holds a single frequency
    """
    freq: float | np.float64 = None
    amp: float | np.float64 = None
    phase: float | np.float64 = None

    model: Callable[[float | np.float64 | list | np.ndarray, float | np.float64, float | np.float64, float | np.float64], list | np.ndarray] = sinusoidal

    def evaluate(self, x : float | np.float64 | list | np.ndarray):
        return self.model(x, self.freq, self.amp, self.phase)