from connect4 import Connect4
from gametree import GameTreeNode, generate_tree
from evalfunctions import random_importance,sliding_opp
import os

all_leafs = []



def expand_tree(c4_node, max_depth, eval_func):
    if not all_leafs:
        generate_tree(None, c4_node, True, max_depth, eval_func)
    else:
        for node in all_leafs:
            generate_tree(None, node, True, max_depth, eval_func)


def cpu_move(c4, max_depth, eval_func):
    root = GameTreeNode(c4)
    expand_tree(root, max_depth, eval_func)
    
    best_val = float('inf')
    best_mv = None
    for child in root.children:
        if child.minmaxval < best_val:
            best_val = child.minmaxval
            best_mv = child.curr
    
    return best_mv


def clear():
    os.system('cls')

def main():
    c4 = Connect4()

    while True:
        c4.pretty_print()
        print("SCORE:",sliding_opp(c4))

        if c4.value == float('-inf'):
            print("CPU WINS!!!")
            return

        while True:
            try: 
                mv = int(input("Pick a column: "))
                c4 = c4.make_move(mv, 1)
                break
            except Exception:
                print("Please select a valid column")
        
        if c4.value == float('inf'):
            c4.pretty_print()
            print("PLAYER WINS!!!")
            return

        c4 = cpu_move(c4, 4, sliding_opp)

        #clear()



if __name__ == "__main__":
    main()