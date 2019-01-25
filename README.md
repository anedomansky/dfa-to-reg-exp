# DFA-to-RegExp
Convert DFAs into regular expressions using the transitive closure method in Python 3.

## Installation

`git clone https://github.com/anedomansky/dfa-to-reg-exp.git`

Remove definitions from the `./automaton-definitions`
OR
Add new `.xml` automaton definition files from [AtoCC](http://www.atocc.de/cgi-bin/atocc/site.cgi?lang=en&site=main) to the `./automaton-definitions`

## Usage

`cd dfa-to-reg-exp`

example script call:

`python main.py ./automaton-definitions/automaton_two_states_one_final_book_example.xml`

## Requirements

* Python 3 interpreter
* git
* [AtoCC](http://www.atocc.de/cgi-bin/atocc/site.cgi?lang=en&site=main) for creating and exporting the automaton definitions
  
## Creating and exporting automaton definitions

1. execute the 'Starte AutoEdit.exe'
2. New
3. Next
4. Add alphabet items
5. Add states (use the default naming e.g. 'q_0') !!!
6. Design the transition graph
7. File -> Export -> Automaton Definition XML
8. Place the created file in `./automaton-definitions/name_of_definition_file.xml