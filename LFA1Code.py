import random

class Grammar:
    def __init__(self):
        self.P = {
            'S': ['dA'],
            'A': ['aB', 'b'],
            'B': ['bC', 'd'],
            'C': ['cB', 'aA']
        }

    def generate_string(self, symbol, length):
        if length == 0:
            return ""
        production = random.choice(self.P.get(symbol, ['']))
        result = ""
        for s in production:
            result += self.generate_string(s, length - 1)
        return result

    def generate_valid_strings(self, count, length):
        valid_strings = []
        for _ in range(count):
            valid_strings.append(self.generate_string('S', length))
        return valid_strings

class FiniteAutomaton:
    def __init__(self, grammar):
        self.transitions = {}
        for state in grammar.P:
            self.transitions[state] = {}
            for prod in grammar.P[state]:
                if len(prod) > 1:
                    self.transitions[state][prod[1]] = prod[0]

    def can_generate_string(self, string):
        current_state = 'S'
        for symbol in string:
            if symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state].get(symbol, None)
            if current_state is None:
                return False
        return current_state == 'S'

# Example usage
grammar = Grammar()
automaton = FiniteAutomaton(grammar)

print("Valid Strings:")
valid_strings = grammar.generate_valid_strings(5, 10)
for s in valid_strings:
    print(s)

print("\nChecking if strings are valid via Finite Automaton:")
for s in valid_strings:
    print(f"'{s}' is valid:", automaton.can_generate_string(s))
