class TransitiveClosure:
    """ 
        Calculates the transitive closure
    """
    def __init__(self, r0, stateInfo):
        self.rK = [row[:] for row in r0]
        self.rKMinusOne = r0
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.regExp = ''
    
    def closure(self, outputFile):
        """ 
            Rk(i,j) = Rk-1(i,j) + Rk-1(i,k)(Rk-1(k,k))*Rk-1(k,j)

            rK: a two dimensional list
            rKMinusOne: a two dimensional list
        """
        # outputFile.write('R0 :')
        # outputFile.write(str(self.rKMinusOne))
        # outputFile.write('\n')
        for k in range(1, self.states + 1):
            self.rKMinusOne = [row[:] for row in self.rK]
            for i in range(1, self.states + 1):
                for j in range(1, self.states + 1):
                    self.rK[i][j] = '(' + self.rKMinusOne[i][j] + ')+(' + self.rKMinusOne[i][k] + ')(' + self.rKMinusOne[k][k] + ')*(' + self.rKMinusOne[k][j] + ')'
            outputFile.write('k = ')
            outputFile.write(str(k))
            outputFile.write(':')
            outputFile.write(str(self.rK))
            outputFile.write('\n')
    
    def getFinalRegExp(self, outputFile):
        """
            1. Look through all states and find the initial state and the final state
            2. Get the regular expression out of the Rk two dimensional list
            
            Returns the final regular expression
        """
        self.closure(outputFile)
        # initialize with out of scope int (valid states are starting at 1)
        initialState = 0
        finalState = 0
        for state in self.stateInfo:
            if(state['isInitial'] and state['isFinal']):
                initialState = state['name']
                finalState = state['name']
            elif(state['isInitial']):
                initialState = state['name']
            elif(state['isFinal']):
                finalState = state['name']
        self.regExp = self.rK[initialState][finalState]
        return self.regExp