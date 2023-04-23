import os

class RegexValidation:
    def __init__(self, transitions, initial_state, final_state):
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_state = final_state

    def clear_screen(self):
        os.system("cls")

    def validate_input(self, input_string, current_state):
        # Check if end of string has been reached
        if input_string == "" and current_state == self.final_state:
            return True

        # Check if current state has a transition with the current symbol
        for transition in self.transitions:
            if transition[0] == current_state and (transition[1] == input_string[0] or transition[1] is None):
                # Explore transition
                for next_state in self.transitions[transition]:
                    if self.validate_input(input_string[1:], next_state):
                        return True

        # No valid transitions found
        return False

    def run(self):
        while True:
            self.clear_screen()
            print(f"Initial state: {self.initial_state}, final state: {self.final_state}")
            input_string = input("Insert a string: ")
            if self.validate_input(input_string, self.initial_state):
                print(f"The string '{input_string}' is valid.")
            else:
                print(f"The string '{input_string}' is invalid.")
            input("\nPress any key to continue...")


transitions = {
    (0, None): {1},
    (1, None): {2, 4, 6},
    (2, 'a'): {3},
    (4, 'b'): {5},
    (3, None): {6},
    (5, None): {6},
    (6, None): {1},
    (6, '$'): {7},
}

rv = RegexValidation(transitions, 0, 7)
rv.run()
