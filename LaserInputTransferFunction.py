from sympy import Matrix

from TransferFunction import TransferFunction


class LaserTransferFunction(TransferFunction):

    output_state = Matrix([[1,0]])

    def compute(self, inputdata):
        return self.output_state