from sympy import Matrix

from TransferFunction import TransferFunction


class BeamSplitterTransferFunction(TransferFunction):
    def compute(self, inputdata):
        m = Matrix([[1, 1], [1, -1]])
        res = inputdata * m

        res = res * (1/res.norm())

        return res