class TransitiveClosure:
    def __init__(self, r0, stateInfo):
        self.rK = [row[:] for row in r0]
        self.rKMinusOne = r0
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.regExp = ''
    
    def closure(self):
        for k in range(1, self.states + 1):
            self.rKMinusOne = [row[:] for row in self.rK]
            for i in range(1, self.states + 1):
                for j in range(1, self.states + 1):
                    self.rK[i][j] = self.rKMinusOne[i][j] + '+' + self.rKMinusOne[i][k] + '(' + self.rKMinusOne[k][k] + ')*' + self.rKMinusOne[k][j]
    
    def getFinalRegExp(self):
        self.closure()
        for state in self.stateInfo:
            if(state['isInitial']):
                initialState = state['name']
            elif(state['isFinal']):
                finalState = state['name']
        for i in range(1, self.states + 1):
            if(finalState == i):
                self.regExp = self.rKMinusOne[initialState][i]
        return self.regExp