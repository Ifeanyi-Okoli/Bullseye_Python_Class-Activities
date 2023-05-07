#Name space is the accessibility of an object within a scope.add()
# Types of namespaces are BuiltinNamespaces, GlobalNamespaces, LocalNamespaces
# Types of import are Absolute import and Relative import

from modulesactiviies import *

num = 0

def checkNum(self):
    # Local Name Space
    global num
    num += 1
    return num

print(checkNum())
