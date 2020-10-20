# Create a binary tree
# Create a class called Tree that has a "root" instance variable of type Node
# Also, define a get_root method that returns the root node.

# Check if left or right child exist
# Added functions that assign a left child or right child

class Tree(object): # class inherits from object
    def __init__(self, node): # constructor
        self.root = node

    def set_root(self, node):
        self.root = node 

    def get_root(self):
        return self.root.value

    def get_left_of_root(self):
        return self.root.get_left_child()

    def get_right_root(self):
        return self.root.get_right_child()


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left.value
    
    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right.value
    
    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None  
    
    def has_right_child(self):
        return self.right != None
        
#Check User

# Creating Nodes for the Tree
node0 = Node("Apple")
node1 = Node("Banana")
node2 = Node("Orange")

print("adding left and right child")
# node 0 will point to node 1
node0.set_left_child(node1)
# now lets point node0 to node2
node0.set_right_child(node2)

# In Short and sweet representation
print("\n---In Short and sweet representation---")
print(f'''
node 0 :                {node0.get_value()}
node 0 : left child  :  {node0.get_left_child()}
node 0 : right child :  {node0.get_right_child()}
''')

print('\nTree Part')
print('''------User inputs an actual node. User will create node, set left and right child. \n The purpose of the TREE class is just to point to the head(I mean root)
# We can access the left and right child as well.''')
tree = Tree(node0)
print("Root Node is: ")
print(tree.get_root())    

print("------END OF STORY-----below are experiment")

print('We can access the Node class\'s get_left_child() getter/setter methods from our tree class by self.root.get_left_child()')
print('Then we have to define an appropriate defination if we want to access it and call this defination in the Tree class and use it like below: ')
print("Left Node is: ", tree.get_left_of_root())
print("Right Node is: ", tree.get_right_root())

# we cannot access the above left and right nodes directly from the Node class using Tree Class object. 
# Will give---> AttributeError: 'Tree' object has no attribute 'get_left_child'
# print("Right Node is: ", tree.get_left_child())


