from pytest import fixture 

import numpy as np

from qdlearn.containers import Grid, Cell 

@fixture 
def grid():
    bounds = np.vstack((np.zeros(3), np.ones(3)))
    mesh = 10 * np.ones(3)
    return Grid(bounds, mesh)


@fixture 
def cell():
    return Cell()