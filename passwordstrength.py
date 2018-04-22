import re
from math import log

numeric=re.compile('\d')
loweralpha=re.compile('[a-z]')
upperalpha=re.compile('[A-Z]')
symbols = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
# symbols=re.compile('[!@#$%^&*()_+-=\|;:?/.,<>~]')

num_of_symbols=1 # adjust accordingly...

def calculate_entropy(password):
    entropy = 0
    for i in password:
        if numeric.search(password):
            entropy += log(36, 2)
        elif loweralpha.search(password):
            entropy += log(26, 2)
        elif upperalpha.search(password):
            entropy += log(26, 2)
        elif i in symbols:
            entropy += log(num_of_symbols, 2)
    print entropy
    return entropy

def check_validity(password):
    accepted = False
    if len(password) >= 8:
        if numeric.search(password):
            if loweralpha.search(password):
                if upperalpha.search(password):
                    for i in password:
                        if i in symbols:
                            accepted = True
                            print "Accepted."
                            break
                    else:
                        print "Add a special character."
                else:
                    print "Add an upper case letter."
            else:
                print "Add a lower case letter."
        else:
            print "Add a number."
    else:
        print "Too short."


calculate_entropy("")
# check_validity("")
