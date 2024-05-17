from Component import Component
from InputTransferFunction import InputTransferFunction


class Input(Component):
    def __init__(self, *next):
        self.set_component_name("Input")
        super().__init__(*next)
        self.set_transfer_function(InputTransferFunction())
