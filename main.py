from Amplifier import Amplifier
from BeamSplitter import BeamSplitter
from Circuit import Circuit
from Input import Input
from LaserInput import LaserInput
from Output import Output
from PhaseShift import PhaseShift

circ = Circuit()

out = Output()

#ps = PhaseShift(out)

bs = BeamSplitter(out)

inp = LaserInput(bs)

circ.add_component(out)
circ.add_component(bs)

circ.set_input_component(inp)
circ.reset_circuit()

circ.simulate()