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

def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    #start at the root node, visit it and the add it to the stack
    node = tree.get_root()
    stack.push(node)
    node = stack.peek()
    # Visit node
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit):
        print(f"""
        Visit Order: {visit_order}
        Stack:
        {stack}
        """)   

        count += 1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node) 
            #Repetative but still
            node = stack.peek()
            visit_order.append(node.get_value())

        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            #print("Pushed to stack: ", node)
            node = stack.peek()           
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.isEmpty():
                node = stack.peek()
            else:
                node = None        


# Driver 
# Tree with nodes'

tree = Tree("Google")
print('                                ',tree.get_root())

tree.get_root().set_left_child(Node("Amazon"))
print('              Left Child: ', tree.get_root().get_left_child())   

tree.get_root().set_right_child(Node("Microsoft"))
print('                                            Right Child: ',tree.get_root().get_right_child()) 

tree.get_root().get_left_child().set_left_child(Node("SpaceX"))
print('Left Left Child: ', tree.get_root().get_left_child().get_left_child())

pre_order_with_stack_buggy(tree)

# the issue here is SpaceX is visited 2 more times because the loop is re occuring in left child forever. We can solve this issue with Track State