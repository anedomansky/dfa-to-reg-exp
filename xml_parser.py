import xml.etree.ElementTree as ET

class XMLParser:
    """ 
        Parsing of any automaton definition .xml file that has been created by AtoCC
    """
    def __init__(self, filename):
        self.filename = filename
        self.file = ET.parse(filename)
        self.root = self.file.getroot()
        self.states = []
        self.alphabet = []

    def getStateInfo(self):
        """ 
            Creation of the states with all necessary information:
                name
                    transforms the default String q_0 into an Integer 1
                                                  q_1 into an Integer 2
                                                  ...
                transitions
                    list of dicts -> [{target : name_of_the_state, symbols: list_of_Strings}, {...}, ...]
                isFinal
                    a Boolean that indicates a final state
                isInitial
                    a Boolean that indicates a initial state

        """
        for state in self.root.findall('STATE'):
            name = state.get('name')
            name = int(name[2:]) + 1
            transitions = []
            for transition in state.findall('TRANSITION'):
                target = transition.get('target')
                target = int(target[2:]) + 1
                symbols = []
                for label in transition.findall('LABEL'):
                    symbols.append(label.get('read'))
                transitionInfo = { 'target': target, 'symbols': symbols }
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
        """ 
            Returns the alphabet of the automaton as a list of Strings
        """
        for a in self.root.find('ALPHABET').findall('ITEM'):
            a = a.get('value')
            self.alphabet.append(a)
        return self.alphabet