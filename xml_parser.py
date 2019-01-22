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
            transitions = []
            for transition in state.findall('TRANSITION'):
                target = transition.get('target')
                symbol = transition.find('LABEL').get('read')
                transitionInfo = { 'target': target, 'symbol': symbol }
                transitions.append(transitionInfo)
            if(state.get('finalstate') == 'true'):
                isFinal = True
            else:
                isFinal = False
            currentState = { 'name': name, 'transitions': transitions, 'isFinal': isFinal }
            self.states.append(currentState)
        return self.states

    def getAlphabet(self):
        for a in self.root.find('ALPHABET').findall('ITEM'):
            a = a.get('value')
            self.alphabet.append(a)
        return self.alphabet