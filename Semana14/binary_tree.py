class Node():
    def __init__(self, Data):
        self.data=Data 
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self, root):
        self.root=Node(root)

    def show_tree(self, traversal_type):
        if traversal_type== "pre-order":
            return self.PreOrder_show(tree.root, "")
        
        else:
            print(f"Traversal {traversal_type} is not the same.")
            return False
        
    def PreOrder_show(self, start, traversal):
        if start is not None:
            traversal+= (f"{start.data} ╰┈➤ ")
            traversal=self.PreOrder_show(start.left, traversal)
            traversal=self.PreOrder_show(start.right, traversal)
        return traversal
        

tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.show_tree("pre-order"))