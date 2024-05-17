from Component import Component


class Circuit():
    the_circuit = list()
    input_component = None


    def add_component(self, component):
        self.the_circuit.append(component)

    def set_input_component(self, input_component):
        print("Set input component to " + str(input_component))
        self.input_component = input_component

    def get_components(self):
        return self.the_circuit

    def print_circuit(self):

        c: Component
        s = "{}   -> {}".format(self.input_component.get_component_name(), self.input_component.get_all_next())

        for c in self.the_circuit:
            s = "{}   -> {}".format(c.get_component_name(), c.get_all_next())
            print(s)

    def clear_visited(self):
        c : Component
        for c in self.the_circuit:
            c.clear_visited()

    def reset_circuit(self):
        self.clear_visited()

    def get_input_component(self):
        return self.input_component

    def simulate(self):
        if self.input_component is None:
            print("No input component defined. Aborting...")
            return
        else:
            queue = list()
            queue.append(self.input_component)
            comp : Component
            comp = None

            while not (len(queue) == 0):
                comp = queue.pop()
                comp.simulate()
                comp.set_visited()

                child : Component
                child = comp.get_unvisited_next()
                while child:
                    print("Visiting " + child.get_component_name())
                    child.set_visited()
                    queue.append(child)
                    child = comp.get_unvisited_next()