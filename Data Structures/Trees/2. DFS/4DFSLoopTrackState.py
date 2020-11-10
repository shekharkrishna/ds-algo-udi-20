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
        return self.left  # PJ: We are calling this method as Node object in the Tree class object and the pointer thing is abstracted and
        # playing with value directly so we remove value and dont need to conver pointer location to value (Dont have to DO: return self.left.value)

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


class Tree(object):  # class inherits from object
    def __init__(self, value=None):  # constructor
        self.root = Node(value)

    def get_root(self):
        return self.root

# Let's define a stack to help keep track of the tree nodes


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item)
                                               for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s  # since i didnt return, i had an error of none type before. So dont forget to return s


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    # start at the root node, visit it and the add it to the stack
    node = tree.get_root()

    # node = stack.peek()
    # Visit node
    visit_order.append(node.get_value())

    # Now we dont just push nodes to the stack for we push state that have node object pushed in to the stack.
    state = State(node)
    stack.push(state)

    count = 0

    while(node):
        if debug_mode:
            print(f"""
            loop count: {count}
            current node: {node}
            Stack:
            {stack}
            """)

        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()  # we make state for that node visited!
            node = node.get_left_child()
            visit_order.append(node.get_value())

            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())

            state = State(node)
            # stack.push(state)

            # stack.push(node)
            # print("Pushed to stack: ", node)
            # node = stack.peek()

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode: # Had issues with indenting and was only getting to 2nd node. This is printed after the loop and will get the final visit order 
        print(f"""
        loop count: {count}
        current node: {node}
        visit order: {visit_order} # Finally Done
        Stack:
        {stack}
        """)
    return visit_order


# Driver
# Tree with nodes'

tree = Tree("Google")
print('                                ', tree.get_root())

tree.get_root().set_left_child(Node("Amazon"))
print('              Left Child: ', tree.get_root().get_left_child())

tree.get_root().set_right_child(Node("Microsoft"))
print('                                            Right Child: ',
      tree.get_root().get_right_child())

tree.get_root().get_left_child().set_left_child(Node("SpaceX"))
print('Left Left Child: ', tree.get_root().get_left_child().get_left_child())


pre_order_with_stack(tree, debug_mode=True)
