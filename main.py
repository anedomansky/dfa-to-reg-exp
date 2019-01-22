import xml_parser

file = xml_parser.XMLParser('./automaton-definitions/automaton_two_states_one_final.xml')

print(file)
print(file.getStateInfo())