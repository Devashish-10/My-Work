class TuringMachine:
    """A Turing machine simulator."""

    def __init__(self, tape, states, transitions, start_state, halt_state):
        """
        Initializes the Turing machine.

        Args:
            tape: A list of symbols on the tape.
            states: A set of states the machine can be in.
            transitions: A dictionary of transitions, where each key is a pair of (state, symbol) and each value is a tuple of (new_state, new_symbol, direction).
            start_state: The initial state of the machine.
            halt_state: The state in which the machine halts.
        """

        self.tape = tape
        self.states = states
        self.transitions = transitions
        self.state = start_state
        self.head_position = 0
        self.halt_state = halt_state

    def step(self):
        """
        Simulates a single step of the Turing machine.

        Returns:
            True if the machine halts, False otherwise.
        """

        current_state = self.state
        current_symbol = self.tape[self.head_position]

        # Find the transition rule for the current state and symbol.
        transition = self.transitions[(current_state, current_symbol)]

        # Update the state, symbol, and head position.
        self.state = transition[0]
        self.tape[self.head_position] = transition[1]
        self.head_position += transition[2]

        # Return True if the machine halts.
        return self.state == self.halt_state

    def run(self):
        """
        Simulates the Turing machine until it halts.
        """

        while not self.step():
            pass

        return self.tape


def main():
    """
    Simulates a simple Turing machine.
    """

    tape = ["0", "1", "0", "1", "0"]
    states = {"q0", "q1", "halt"}
    transitions = {
        ("q0", "0"): ("q1", "1", "R"),
        ("q1", "0"): ("q0", "0", "L"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q0", "halt"): ("halt", "halt", "*"),
        ("q1", "halt"): ("halt", "halt", "*"),
    }
    start_state = "q0"
    halt_state = "halt"

    turing_machine = TuringMachine(tape, states, transitions, start_state, halt_state)

    # Simulate the Turing machine until it halts.
    output_tape = turing_machine.run()

    # Print the output tape.
    print(output_tape)


if __name__ == "__main__":
    main()