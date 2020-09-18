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
        return self.left
    
    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right
    
    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None
        # if self.left != None:
        #     return True
        # else: 
        #     return False
    
    def has_right_child(self):
        return self.right != None
        # if self.right != None:
        #     return True
        # else: 
        #     return False

#Check 
node0 = Node("Apple")
node1 = Node("Banana")
node2 = Node("Orange")

print(f"has left child? {node0.has_left_child()}") 
print(f"has right child? {node0.has_right_child()}")


print("adding left and right child")
# node 0 will point to node 1
node0.set_left_child(node1)
# now lets point node0 to node2
node0.set_right_child(node2)

# In Short and sweet representation
print("\n---In Short and sweet representation---")
print(f'''
node 0 :                {node0.value}
node 0 : left child  :  {node0.left.value}
node 0 : right child :  {node0.right.value}
''')

print(f"has left child? {node0.has_left_child()}") 
print(f"has right child? {node0.has_right_child()}")
print("Node1 has left and right child?")
print(node1.has_left_child())
print(node1.has_right_child())







    