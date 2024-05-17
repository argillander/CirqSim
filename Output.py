from Component import Component
from OutputTransferFunction import OutputTransferFunction


class Output(Component):

    def __init__(self, *next):
        super().__init__(*next)
        self.set_component_name("Output")
        self.set_transfer_function(OutputTransferFunction())
