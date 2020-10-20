# Adding functions to set and get the value of the node

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

# Using constructor to set the value of the Node
node0 = Node("Google")
print(node0.value)
# this function get value with give the value set by the default constuctor
print(node0.get_value())

# Using setter to set the value of the Node | As like in JAVA, using function set_value() 
# that will set the value of the node
node0.set_value('Amazon')
print(node0.get_value())
    
     
