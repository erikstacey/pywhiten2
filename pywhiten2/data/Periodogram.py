import numpy as np
from dataclasses import dataclass

@dataclass
class Periodogram:
    frequencies : np.ndarray[np.float64]
    amplitudes : np.ndarray[np.float64]
