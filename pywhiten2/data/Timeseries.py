import numpy as np
from dataclasses import dataclass

@dataclass
class Timeseries:
    time : np.ndarray[np.float64]
    data : np.ndarray[np.float64]
    weights : np.ndarray[np.float64]
    