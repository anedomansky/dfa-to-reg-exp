import xml_parser
import initialization

file = xml_parser.XMLParser('./automaton-definitions/automaton_two_states_one_final.xml')
stateInfo = file.getStateInfo()
alphabet = file.getAlphabet()
initializer = initialization.Initialization(stateInfo)




print(file)
print(stateInfo)
print(alphabet)
print(initializer.initialize())