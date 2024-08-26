class GameTreeNode:
  def __init__(self, state):
    self.curr = state
    self.children = None
    self.parent = None
    self.minmaxval = None


def generate_tree(par, root, is_min, depth, evaluation_function):
  if depth == 0:
    root.minmaxval = evaluation_function(root.curr)
    return root.minmaxval
  
  if is_min:
    root.children = [GameTreeNode(child) for child in root.curr.successors(2)]
  else:
    root.children = [GameTreeNode(child) for child in root.curr.successors(1)]

  if not root.children:
    root.minmaxval = root.curr.value
    return root.minmaxval

  if par:
    root.parent = par

  for i in range(len(root.children)):
    val = generate_tree(root, root.children[i], not is_min, depth - 1, evaluation_function)
    root.children[i].minmaxval = val

  if is_min:
    mn = float('inf')
    best_chld = None
    for child in root.children:
      if child.minmaxval < mn:
        best_chld = child
        mn = child.minmaxval
    
    root.minmaxval = mn
    return root.minmaxval
    #root.children = [best_chld]
  else:
    mx = float('-inf')
    for child in root.children:
      mx = max(mx, child.minmaxval)
    root.minmaxval = mx
    return root.minmaxval





