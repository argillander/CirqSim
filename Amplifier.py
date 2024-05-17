from AmplifierTransferFunction import AmplifierTransferFunction
from Component import Component


class Amplifier(Component):

    def __init__(self, *next):
        super().__init__(*next)
        self.set_component_name("Amplifier")
        self.set_transfer_function(AmplifierTransferFunction())