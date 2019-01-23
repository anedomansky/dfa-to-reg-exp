import sys
import xml_parser
import initialization
import transitive_closure

if(len(sys.argv) > 1):
    file = xml_parser.XMLParser(sys.argv[1])
else:
    print('The automaton file could not be read or does not exist.')

stateInfo = file.getStateInfo()
alphabet = file.getAlphabet()
initializer = initialization.Initialization(stateInfo)
r0 = initializer.initialize(alphabet)
transitiveClosure = transitive_closure.TransitiveClosure(r0, stateInfo)
finalRegExp = transitiveClosure.getFinalRegExp()




print(stateInfo)
print(alphabet)
print(r0)
print(finalRegExp)