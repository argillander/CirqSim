import TransferFunction


class Component():
    component_name = ""
    next_components = list()

    input_val = 0.0
    output_val = 0.0

    transfer_function: TransferFunction = 0.0

    visited = False

    def __init__(self, *next):
        for c in next:
            print("Connecting the output of " + self.component_name + " to " + str(c))
            self.next_components.append(c)


    def get_input_val(self):
        return self.input_val

    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

    def is_visited(self):
        return self.visited

    def get_component_name(self):
        return self.component_name

    def set_transfer_function(self, tf):
        self.transfer_function = tf

    def set_component_name(self, name):
        self.component_name = name

    def get_all_next(self):
        return self.next_components

    def get_unvisited_next(self):
        unvisited = list()
        unvisited = [c for c in self.next_components if not c.is_visited()]
        if len(unvisited) == 0:
            return None
        else:
            return unvisited[0]

    def has_next(self):
        return not (len(self.unvisited) == 0)

    def simulate(self):
        print("Simulating " + self.component_name)
        self.output_val = self.transfer_function.compute(self.input_val)

        c: Component
        for c in self.next_components:
            if c:
               # print(self.component_name +": Setting " + str(c) + "'s input val to " + str(self.output_val))
                c.input_val = self.output_val

        print(self.component_name + " in={}, out={}".format(self.input_val, self.output_val))

