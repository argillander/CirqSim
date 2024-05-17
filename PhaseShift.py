from sympy import Matrix

from Component import Component
from TransferFunction import TransferFunction

import math
import cmath

class PhaseShiftTransferFunction(TransferFunction):

    angle = math.pi/2

    def compute(self, inputdata):
        coeff = cmath.exp(self.angle * 1.0j)
        m = Matrix([[1, 0], [0, coeff]])

        res = inputdata * m
        res = res * (1/res.norm())

        return res


class PhaseShift(Component):

    def __init__(self, *next):
        self.set_component_name("BeamSplitter5050")
        super().__init__(*next)
        self.set_transfer_function(PhaseShiftTransferFunction())
