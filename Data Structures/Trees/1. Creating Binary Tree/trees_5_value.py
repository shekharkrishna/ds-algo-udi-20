# Create a binary tree
# Create a class called Tree that has a "root" instance variable of type Node
# Also, define a get_root method that returns the root node.

# Check if left or right child exist
# Added functions that assign a left child or right child


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
        return self.left # PJ: We are calling this method as Node object in the Tree class object and the pointer thing is abstracted and 
        #playing with value directly so we remove value and dont need to conver pointer location to value (Dont have to DO: return self.left.value)
    
    def set_left_child(self, node):
        self.left = node 

    def get_right_child(self):
        return self.right
    
    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None  
    
    def has_right_child(self):
        return self.right != None

    def __str__(self): 
        return  'Pointer *--> ' + self.value  + self.get_value()


class Tree(object): # class inherits from object
    def __init__(self, node): # constructor
        self.root = Node(node)

    def set_root(self, node):
        self.root = Node(node) 

    def get_root(self):
        return self.root # PJ: Either use self.root.value or 
        # better generalization and abstraction of pointers by __str__ in Node Class not This TREE Class

    def set_left_child(self, left):
        self.root.set_left_child(left)        

    def set_right_child(self, right):
        self.root.set_right_child(right)         

    def get_left_of_root(self):
        return self.root.left

    def get_right_root(self):
        return self.root.get_right_child()   

        
#Check User
tree = Tree('Amazon')
print("Root Node is: ")
print(tree.get_root())    

print("...........adding left and right child")
# node 0 will point to node 1
tree.set_left_child('Google')
# now lets point node0 to node2
tree.set_right_child('Facebook')

print("Left Node is: ", tree.get_left_of_root())
print("Right Node is: ", tree.get_right_root())