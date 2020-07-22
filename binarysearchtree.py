class Node(object):
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, val=None):
        node = Node(val)
        self.root = node
    
    def insert(self, val):
        curr_node = self.root

        while True:
            if curr_node is None:
                curr_node = Node(val)
                break
            else:
                if val <= curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = Node(val)
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = Node(val)
                        break
                    else:
                        curr_node = curr_node.right



    def traversal(self, node=None):
        if node is None:
            print('')
        else:
            print('c', node.value)        
            curr_node = node
            if curr_node.left is not None:
                print('going left')
                curr_node = curr_node.left
                self.traversal(curr_node)
            
            curr_node = node
            print('m', curr_node.value)
            if curr_node.right is not None:
                print('going right')
                curr_node = curr_node.right
                self.traversal(curr_node)
            print('goint to parent')
            # return

    def lookup(self, val):
        curr_node = self.root
        if curr_node is None:
            return False
        while curr_node is not None:
            if val == curr_node.value:
                return curr_node
            elif val < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return False
      
a = BST(val=2)
a.insert(3)
a.insert(1)
a.insert(0)
a.insert(1.5)
a.insert(5)
# a.traversal(node=a.root)
a.traversal(a.lookup(1))