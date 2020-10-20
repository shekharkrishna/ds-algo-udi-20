#Define a node

class Node(object): #going to inherit from object
    def __init__(self, value=None): # constructor that dont take any argument so just a self    
        # Step 2: for a contructor that takes a value and if in case it doesn't, default value to none.
        self.value = value #instance variables
        self.left = None
        self.right = None   

# Adding a constructor that takes the value as a parameter
node0 = Node()
print(f""" 
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

# Another instance of Node as node0
node0 = Node('Apple')
print(f""" 
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

