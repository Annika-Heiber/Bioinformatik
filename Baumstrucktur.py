class Tree:
  def __init__(self, val = None):
    if val != None:
        self.val = val
    else:
        self.val = None
        
    self.left = None
    self.right = None
    
tree = Tree(20)
tree.left = Tree(18)
tree.right = Tree(22)

print(tree.left.val)
print(tree.right.val)