class Initialization:
    """ 
        Creation of R0 

        k = 0
        All paths without any additional nodes between i and j
    """
    def __init__(self, stateInfo):
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)
        self.r0 = [['-'] * (self.states + 1) for i in range(self.states + 1)]

    def initialize(self, alphabet):
        """ 
            Case 1:
                Direct path from i to j over one edge
            Case 2:
                A path with the length 0, goes from i to i

            If i != j then only case 1 is possible
                test whether symbols exist to satisfy case 1
                    a) no symbol exists -> R0(i,j) = null
                    b) one symbol exists -> R0(i,j) = a
                    c) more than one symbol exists -> R0(i,j) = a1 + a2 + ... + aK
            If i == j then only case 2 is possible
                test whether symbols exists to satisfy case 2
                    a) no symbol exists -> R0(i,j) = e
                    b) one symbol exists -> R0(i,j) = e + a
                    c) more than one symbol exists -> R0(i,j) = e + a1 + a2 + ... + aK         
        """
        for i in range(1, self.states + 1):
            for j in range(1, self.states + 1):
                if(i == j):
                    self.r0[i][j] = 'e'
                else:
                    self.r0[i][j] = 'null'
                for a in alphabet:
                    if(self.hasTransition(i, a, j) and self.r0[i][j] == 'null'):
                        self.r0[i][j] = a
                    elif(self.hasTransition(i, a, j) and self.r0[i][j] != 'null'):
                        self.r0[i][j] += '+' + a
        return self.r0
    
    def hasTransition(self, i, a, j):
        """
            Checks whether a transition between i and j exists
        """
        for state in self.stateInfo:
            if(state['name'] == i):
                for transition in state['transitions']:
                    if(transition['target'] == j and a in transition['symbols']):
                        return True
        return False

            