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

def pre_order(tree):
    visit_order = list()
    return visit_order
    



tree = Tree("Google")
print('                                ', tree.get_root())

tree.get_root().set_left_child(Node("Amazon"))
print('              Left Child: ', tree.get_root().get_left_child())

tree.get_root().set_right_child(Node("Microsoft"))
print('                                            Right Child: ',
      tree.get_root().get_right_child())

tree.get_root().get_left_child().set_left_child(Node("SpaceX"))
print('Left Left Child: ', tree.get_root().get_left_child().get_left_child())

print(pre_order(tree))