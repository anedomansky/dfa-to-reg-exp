class Initialization:
    def __init__(self, stateInfo):
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.r0 = [['-'] * (self.states + 1) for i in range(self.states + 1)]

    def initialize(self, alphabet):
        for i in range(1, self.states + 1):
            for j in range(1, self.states + 1):
                if(i == j):
                    self.r0[i][j] = 'e'
                else:
                    self.r0[i][j] = 'null'
                for a in alphabet:
                    if(self.isTransition(i, a, j)):
                        self.r0[i][j] += '+' + a
        return self.r0
    
    def isTransition(self, i, a, j):
        for state in self.stateInfo:
            if(state['name'] == i):
                for transition in state['transitions']:
                    if(transition['target'] == j and transition['symbol'] == a):
                        return True
        return False

            