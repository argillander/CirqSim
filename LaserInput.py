from Component import Component
from LaserInputTransferFunction import LaserTransferFunction


class LaserInput(Component):

    def __init__(self, *next):
        self.set_component_name("LaserInput")
        super().__init__(*next)
        self.set_transfer_function(LaserTransferFunction())
