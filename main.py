import sys
import xml_parser
import initialization
import transitive_closure

if(len(sys.argv) > 1):
    file = xml_parser.XMLParser(sys.argv[1])
else:
    print('The automaton file could not be read or does not exist.')

conversionOutputFile = open('./conversion/' + sys.argv[1].replace('./automaton-definitions/', '') + '.txt', 'w')
conversionOutputFile.write('##### Information about the states              #####\n')
stateInfo = file.getStateInfo()
conversionOutputFile.write(str(stateInfo))
conversionOutputFile.write('\n##### Available alphabet                        #####\n')
alphabet = file.getAlphabet()
conversionOutputFile.write(str(alphabet))
conversionOutputFile.write('\n##### R0                                        #####\n')
initializer = initialization.Initialization(stateInfo)
r0 = initializer.initialize(alphabet)
conversionOutputFile.write(str(r0))
conversionOutputFile.write('\n##### Rk #####\n')
transitiveClosure = transitive_closure.TransitiveClosure(r0, stateInfo)
finalRegExp = transitiveClosure.getFinalRegExp(conversionOutputFile)
conversionOutputFile.write('##### Final regular expression (not simplified) #####\n')
conversionOutputFile.write(finalRegExp)
conversionOutputFile.close()

# print(stateInfo)
# print(alphabet)
# print(r0)
# print(finalRegExp)
