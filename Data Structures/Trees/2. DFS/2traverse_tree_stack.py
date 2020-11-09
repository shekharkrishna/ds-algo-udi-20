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

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Tree(object): # class inherits from object
    def __init__(self, value=None): # constructor
        self.root = Node(value)  

    def get_root(self):
        return self.root

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def __repr__(self):
        return f"Node({self.peek()})"

     def __str__(self):
        return f"Node({self.peek()})"


# Driver 
# Tree with nodes'

visit_order = list()
stack = Stack()

tree = Tree("Google")
print('                                ',tree.get_root())

tree.get_root().set_left_child(Node("Amazon"))
print('              Left Child: ', tree.get_root().get_left_child())   

tree.get_root().set_right_child(Node("Microsoft"))
print('                                            Right Child: ',tree.get_root().get_right_child()) 

tree.get_root().get_left_child().set_left_child(Node("SpaceX"))
print('Left Left Child: ', tree.get_root().get_left_child().get_left_child())

#start at the root node, visit it and the add it to the stack
node = tree.get_root()
stack.push(node)

# Visit node
visit_order.append(node.get_value())

print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")

# Pre Order Traversal BFS
# Check if the node has the left child
print(f"{node} has left child?       {node.has_left_child()}")

# if node has left child, visit it and add it to the stack (Amazon)
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# Visit node list append (Amazon)
visit_order.append(node.get_value())

#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")



#Cycle
# Pre-order Traversal DFS
# Check if the node has the left child
print(f"{node} has left child?       {node.has_left_child()}")

# if node has left child, visit it and add it to the stack (SpaceX)
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# Visit node list append (SpaceX)
visit_order.append(node.get_value())

#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")

# From here, implementing in hurry:

# Check if the node has the left child
print(f"{node} has left child?       {node.has_left_child()}")
print(f"{node} has right child?       {node.has_right_child()}")

if node.has_left_child() == node.has_right_child() == False:
    poped = stack.pop()
    print("Poped from left == right: ", poped)

#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")

# set the node to the new top of the stack
node = stack.peek()
print(f"PJ: New Node set to: {node}")

# Check if the node has the left child
print(f"{node} has left child?       {node.has_left_child()}")
print(f"{node} has right child?       {node.has_right_child()}")

if node.has_left_child() == node.has_right_child() == False:
    poped = stack.pop()
    print("Poped from left == right: ", poped)
if node.has_right_child() == False:
    poped = stack.pop()
    print("Poped from right == False: ", poped)

#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")

# set the node to the new top of the stack
node = stack.peek()
print(f"PJ: New Node set to: {node}")

# now we are at the root node (Google) which has the right child after being done with the left child (Depth First Search - PreOrder)
# Check if the node has the left child
print(f"{node} has left child?       {node.has_left_child()}")
print(f"{node} has right child?       {node.has_right_child()}")

if node.has_right_child(): 
    node = node.get_right_child()
    stack.push(node)
    print("Pushed to stack: ", node)

# Visit node list append (Microsoft)
visit_order.append(node.get_value())

#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")

# check if node (microsoft has left and right child)
print("currdent node: ", node)

print(f"{node} has left child?       {node.has_left_child()}")
print(f"{node} has right child?       {node.has_right_child()}")
# Since it has neither left or right child nodes, we are done tracking it and pop it off the stack
print(f"pop {stack.pop()} off the stack")
#Repeat the print to see
print(f"""
Visit Order: {visit_order}
Stack:
{stack}
""")


# At the top of the stack Google,  we checked its right and left child nodes. but now we can pop it off the stack as well
# We have already traced its triversal path. 
print("Current stack situation: ", stack)
stack.pop()
print("poped off the top node of the stack. Head node")
print("Current stack situation: ", stack.size())
print("Current stack situation: Is it empty? \n", stack.isEmpty())

print(f"\nPre-order traversal visited nodes in this order: {visit_order}")


