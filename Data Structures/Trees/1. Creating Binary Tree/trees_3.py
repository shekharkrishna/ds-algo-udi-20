# Add functions that assign a left child or right child
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
        return self.left
    
    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right
    
    def set_right_child(self, node):
        self.right = node

#Check 
node0 = Node("Apple")
node1 = Node("Banana")
node2 = Node("Orange")

print("Individual Nodes are: which are not pointing to any one  ")
print(node0.get_value())
print(node1.get_value())
print(node2.get_value())

node0.set_left_child(node1) # node 0 will point to node 1

print("Getting the address of the leftchild that Apple or node0 is pointing to")
leftChild = node0.get_left_child() # First instinct
#leftChild = node0.left # Powerful way to get the left pointer address 
print(leftChild)

print("Getting the value of the left child pointed to")
print(leftChild.value) # first instinct plus powerful insight gained 


#now lets point node0 to node2
node0.set_right_child(node2)
print("Getting the address of the right child that Apple or node0 is pointing to")
rightChild = node0.get_right_child() # First instinct
print(rightChild)

print("Getting the value of the right child pointed to")
print(rightChild.value) # first instinct plus powerful insight gained 


# In Short and sweet representation
print("\n---In Short and sweet representation---")
print(f'''
node 0 :                {node0.value}
node 0 : left child  :  {node0.left.value}
node 0 : right child :  {node0.right.value}
''')







    