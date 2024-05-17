from TransferFunction import TransferFunction


class AmplifierTransferFunction(TransferFunction):


    gain = 2

    def compute(self, input_data):
        return self.gain * input_data

    def set_gain(self, gain):
        self.gain = gain