from TransferFunction import TransferFunction


class InputTransferFunction(TransferFunction):

    voltage_level = 10.0

    def compute(self, inputdata):
        return self.voltage_level
