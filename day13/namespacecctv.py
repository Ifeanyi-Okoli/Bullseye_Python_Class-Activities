#Name space is the accessibility of an object within a scope.add()
# Types of namespaces are BuiltinNamespaces, GlobalNamespaces, LocalNamespaces
# Types of import are Absolute import and Relative import
#to modify, edit or mutate a global variable within a local scope, use the global keyword to declare the variable as global within the local scoe.

from modulesactiviies import *

num = 0

def checkNum(x):
    # Local Name Space
    global num
    num += x
    return num

print(checkNum(10))
