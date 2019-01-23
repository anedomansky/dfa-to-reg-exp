import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, filename):
        self.filename = filename
        self.file = ET.parse(filename)
        self.root = self.file.getroot()
        self.states = []
        self.alphabet = []

    def getStateInfo(self):
        for state in self.root.findall('STATE'):
            name = state.get('name')
            name = int(name[2:]) + 1
            transitions = []
            for transition in state.findall('TRANSITION'):
                target = transition.get('target')
                target = int(target[2:]) + 1
                symbol = transition.find('LABEL').get('read')
                transitionInfo = { 'target': target, 'symbol': symbol }
                transitions.append(transitionInfo)
            if(state.get('finalstate') == 'true'):
                isFinal = True
            else:
                isFinal = False
            currentState = { 'name': name, 'transitions': transitions, 'isFinal': isFinal }
            self.states.append(currentState)
        initialState = self.root.find('INITIALSTATE').get('value')
        for state in self.states:
            if(state['name'] == int(initialState[2:])+1):
                state['isInitial'] = True
            else:
                state['isInitial'] = False
        return self.states

    def getAlphabet(self):
        for a in self.root.find('ALPHABET').findall('ITEM'):
            a = a.get('value')
            self.alphabet.append(a)
        return self.alphabet