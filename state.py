# Jack Haugh
# Classes used in Thompson's construction


class State:
    # Every state has 0, 1, or 2 edges from it.
    edges = []

    # Label for the arrows, None means epsilon
    label = None

    # Constructor for the class
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

myinstance = State(label='a', edges=[])
myotherinstance = State(edges=[myinstance])
print(myinstance.label)
print(myotherinstance.edges[0])


class Fragment:
    # Start state of NFA fragment.
    start = None
    # Accept state of NFA fragment.
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    # Convert input to a stack-ish list.
    infix = list(infix) [::-1]

    # Operator stack.
    opers = []

    # Output list.
    postfix = []

    # Operator precedence
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input one character at a time.
    while infix:
        # Pop a character from the input.
        c = infix.pop()
         # Decide what to do based on the character
        if c == '(' :
        # Push c to the operator stack
             opers.append(c)
         elif c == ')':
            # Pop the operators stack until you find an (.
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # Get rid of the '('.
            opers.pop()
        elif c in prec:
            # Push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.push())
        # Push c to the operator stack.
        opers.append(c)
    else:
        # Typically, We just push the character to the output.
        postfix.append(c)
    # Pop all operators to the output.
    while opers:
        postfix.append(opers.pop())
    # Convert output list to string
    return ''.join(postfix)


def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # Pop a character from postfix.
        c = postfix.pop()
        if c == '*':
            # Do something here
        elif c == '.':
            # Do something here
        elif c == '|':
            #Do something here
        else:
            accept = State()
            initial = State(label=c, edges=[accept])
            newfrag = Fragment(initial, accept)
            nfa_stack.append(newfrag)
            



def match(regex, s):
    # This function will return true and only if the regular expression
    # regex (fully) matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA.
    nfa = regex_compile(regex)
    # Ask the NFA if it matches the String s.
    return nfa.match(s)

match("a.b|b*", "bbbbbbbbb")



