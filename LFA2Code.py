class Grammar:
    def __init__(self, P):
        self.P = P

    def classify_chomsky_hierarchy(self):
        if all(len(prod) == 2 for prods in self.P.values() for prod in prods):
            return "Type 2: Context-Free Grammar"
        elif all(len(prod) <= 2 for prods in self.P.values() for prod in prods):
            return "Type 3: Regular Grammar"
        else:
            return "Other"

class FiniteAutomaton:
    def __init__(self, Q, Sigma, delta, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.F = F

    def is_deterministic(self):
        for state in self.Q:
            for symbol in self.Sigma:
                if len(self.delta.get((state, symbol), [])) > 1:
                    return False
        return True

    def convert_to_regular_grammar(self):
        P = {}
        for state, next_state in self.delta.items():
            for symbol in self.Sigma:
                if (state, symbol) in self.delta:
                    ns = self.delta[(state, symbol)]
                    if state not in P:
                        P[state] = []
                    P[state].append(ns + symbol)
        return Grammar(P)

    def convert_to_deterministic(self):
        pass

    def draw_graph(self):
        pass

Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c'}
delta = {
    ('q0', 'a'): 'q1',
    ('q1', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q0', 'a'): 'q0',
    ('q2', 'c'): 'q3',
    ('q3', 'c'): 'q3'
}
F = {'q3'}

fa = FiniteAutomaton(Q, Sigma, delta, F)

print("Chomsky Hierarchy Classification:", fa.convert_to_regular_grammar().classify_chomsky_hierarchy())
print("Deterministic FA?" if fa.is_deterministic() else "Non-deterministic FA")
