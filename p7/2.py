from abc import abstractmethod, ABCMeta


inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

wiring = [] # includes wires and gates
wires = dict() # includes just mapping names to wires or names to names (aliased wires)

def lookup_wire(name):
    wire =  wires.get(name)
    if issubclass(type(wire), str):
        return lookup_wire(wire)
    return wire

class BinaryGate(metaclass=ABCMeta):
    @abstractmethod
    def compute_value(self, lhs_value, rhs_value):
        pass

    def get_value(self):
        if self.value is not None:
            return self.value

        val_one = self.lhs_value
        val_two = self.rhs_value
        if val_one is None:
            wire_one = lookup_wire(self.wire_one)
            if wire_one is None:
                raise Exception('Binary does not have input wire one...')
            val_one = wire_one.get_value()

        if val_two is None:
            wire_two = lookup_wire(self.wire_two)
            if wire_two is None:
                raise Exception('Binary does not have input wire two...')
            val_two = wire_two.get_value()

        if val_one is None or val_two is None:
            return None

        self.value = self.compute_value(val_one, val_two)
        return self.value

    def __init__(self, lhs, rhs):
        self.value = None
        self.wire_one = None
        self.wire_two = None
        self.lhs_value = None
        self.rhs_value = None

        if issubclass(type(lhs), str):
            self.wire_one = lhs
        elif issubclass(type(lhs), int):
            self.lhs_value = lhs
        else:
            raise Exception('BinaryGate initialized with invalid argument')

        if issubclass(type(rhs), str):
            self.wire_two = rhs
        elif issubclass(type(rhs), int):
            self.rhs_value = rhs
        else:
            raise Exception('BinaryGate initialized with invalid argument')

class AndGate(BinaryGate):
    def compute_value(self, lhs_value, rhs_value):
        return lhs_value & rhs_value

class OrGate(BinaryGate):
    def compute_value(self, lhs_value, rhs_value):
        return lhs_value | rhs_value

class LShiftGate(BinaryGate):
    def compute_value(self, lhs_value, rhs_value):
        return lhs_value << rhs_value

class RShiftGate(BinaryGate):
    def compute_value(self, lhs_value, rhs_value):
        return lhs_value >> rhs_value

class UnaryGate(metaclass=ABCMeta):
    @abstractmethod
    def compute_value(self, wire):
        pass

    def get_value(self):
        if self.value is not None:
            return self.value

        wire = lookup_wire(self.wire)
        if wire is None:
            raise Exception('Unary does not have input wire...')

        wire_value = wire.get_value()
        if wire_value is not None:
            self.value = self.compute_value(wire_value)
            return self.value

        return None

    def __init__(self, input):
        self.value = None
        self.wire = None

        if issubclass(type(input), str):
            self.wire = input
        elif issubclass(type(input), int):
            self.value = int(input)
        else:
            raise Exception('UnaryGate initialized with invalid argument')

class NotGate(UnaryGate):
    def compute_value(self, wire):
        return ~wire

class Wire():
    def get_value(self):
        if self.value is not None:
            return self.value

        if self.input_gate is not None:
            self.value = self.input_gate.get_value() # could come back as None
            return self.value

        raise Exception("Wire is not set up properly")

    def __init__(self, input):
        if issubclass(type(input), int):
            self.value = input
            self.input_gate = None
        elif issubclass(type(input), (UnaryGate, BinaryGate)):
            self.value = None
            self.input_gate = input
        else:
            raise Exception('Wire initialized with invalid argument')

def try_parse_int(string, ret = None):
    try:
        return int(string)
    except:
        return ret

def parse_wiring_from_lines(lines):
    for line in lines:
        components = line.split(' ')
        if len(components) == 3:
            # value is provided to wire
            value = try_parse_int(components[0])
            if value is not None:
                wire = Wire(value)
                wires[components[2]] = wire
                wiring.append(wire)
            else:
                # wire is just an alias...
                print('alias', components[0], components[2])
                wires[components[2]] = components[0]
            
        elif len(components) == 4:
            # unary gate
            op = components[0]
            if op == 'NOT':
                not_gate = NotGate(try_parse_int(components[1], components[1]))
                output_wire = Wire(not_gate)
                wires[components[3]] = output_wire
                wiring.append(not_gate)
                wiring.append(output_wire)
        elif len(components) == 5:
            # binary gate
            op = components[1]
            gate = None
            if op == 'AND':
                # other input is also a wire
                gate = AndGate(
                    try_parse_int(components[0], components[0]),
                    try_parse_int(components[2], components[2]))
            elif op == 'OR':
                # other input is also a wire
                gate = OrGate(
                    try_parse_int(components[0], components[0]),
                    try_parse_int(components[2], components[2]))
            elif op == 'LSHIFT':
                # other input is a value
                gate = LShiftGate(
                    try_parse_int(components[0], components[0]),
                    try_parse_int(components[2], components[2]))
            elif op == 'RSHIFT':
                # other input is a value
                gate = RShiftGate(
                    try_parse_int(components[0], components[0]),
                    try_parse_int(components[2], components[2]))

            output_wire = Wire(gate)
            wires[components[4]] = output_wire
            wiring.append(gate)
            wiring.append(output_wire)

parse_wiring_from_lines(inp)

def solve(wiring):
    total_components = len(wiring)
    while True:
        is_component_solved = [ 0 if component.get_value() is None else 1 for component in wiring ]
        solved_count = sum(is_component_solved)
        if solved_count == total_components:
            break

solve(wiring)
wire_a_val = lookup_wire('a').get_value()
print(f'a = {wire_a_val}')

print("now setting b to a's value and resetting all other values, re-running circuit")

wiring = []
wires = dict()
parse_wiring_from_lines(inp)
wires['b'] = Wire(wire_a_val)
solve(wiring)

wire_a_val = lookup_wire('a').get_value()
print(f'a = {wire_a_val}')
