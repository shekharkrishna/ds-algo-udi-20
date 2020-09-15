#Define a node

class Node(object): #going to inherit from object
    def __init__(self): # constructor that dont take any argument so just a self       
        self.value = None
        self.left = None
        self.right = None

node0 = Node()
print(f""" 
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")