class Initialization:
    def __init__(self, stateInfo):
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.r0 = [['-'] * (self.states + 1) for i in range(self.states + 1)]

# TODO: fix the problem with the end exp
    def initialize(self, alphabet):
        for i in range(1, self.states + 1):
            for j in range(1, self.states + 1):
                if(i == j):
                    self.r0[i][j] = 'e'
                else:
                    self.r0[i][j] = 'null'
                for a in alphabet:
                    if(self.hasTransition(i, a, j) and self.r0[i][j] != 'null'):
                        self.r0[i][j] += '+' + a
                    elif(self.hasTransition(i, a, j) and self.r0[i][j] == 'null'):
                        self.r0[i][j] = a
        return self.r0
    
    def hasTransition(self, i, a, j):
        for state in self.stateInfo:
            if(state['name'] == i):
                for transition in state['transitions']:
                    if(transition['target'] == j and a in transition['symbols']):
                        return True
        return False

            