from BeamSplitterTransferFunction import BeamSplitterTransferFunction
from Component import Component


class BeamSplitter(Component):

    def __init__(self, *next):
        self.set_component_name("BeamSplitter5050")
        super().__init__(*next)
        self.set_transfer_function(BeamSplitterTransferFunction())
