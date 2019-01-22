class Initialization:
    def __init__(self, stateInfo):
        self.stateInfo = stateInfo
        self.states = len(self.stateInfo)

    def initialize(self):
        return 1