class Initialization:
    def __init__(self, stateInfo):
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.r0 = {}

    def initialize(self, alphabet):
        for i in self.states:
            for j in self.states:
                if(i == j):
                    self.r0[str(i) + '-' + str(j)] = 'e'
                else:
                    self.r0[str(i) + '-' + str(j)] = '-'
                for a in alphabet:
                    if(self.isTransition(i, a, j)):
                        self.r0[str(i) + '-' + str(j)] += '+' + a
        return 1
    
    def isTransition(self, i, a, j):
        return 1