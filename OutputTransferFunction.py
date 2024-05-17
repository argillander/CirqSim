from sympy import pprint, Matrix
from sympy.physics.quantum import Dagger

from TransferFunction import TransferFunction


class OutputTransferFunction(TransferFunction):

    def compute(self, input_data):
        input_data:Matrix
        print("Output data: " + str(input_data))
        d = Dagger(input_data) * input_data


        pprint(d)
