"""
Pinghang Fan, pfan450. 748224962
avl_trees.py
This is a program that checks if an adjency matrix is an avl tree.
"""
import sys

class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def get_height(root):
    """Base condition when tree is empty"""
    if root is None:
        return 0

    """Recursive call to left and right subtrees"""
    return 1 + max(get_height(root.left), get_height(root.right))

def check_balanced_tree(root):
    """Base condition if tree is empty"""
    if root is None: 
        return True
    return check_balanced_tree(root.right) and check_balanced_tree(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1

def DFS(start, adj_list, visited, avl): 
    #print(start, end = ' ') 
    visited[start] = True
    for i in range(len(visited)): 
        if (adj_list[start][i] == 1 and (not visited[i])): 
            left_root = adj_list[start].index(1)
            right_root = len(adj_list[start]) - 1 - adj_list[start][::-1].index(1)
            if i == left_root:
                avl.left = Tree(avl)
                DFS(i, adj_list, visited, avl.left)
            if i ==  right_root and right_root != left_root:
                avl.right = Tree(avl)
                DFS(i, adj_list, visited, avl.right)
    return avl
            

def main():
    total_list = list()
    adj_list = list()
    """Gettings inputs"""
    for line in sys.stdin:
        if line == "\n":
            break
        if line == None or line == "None\n":
            break
        total_list.append([int(n) for n in line.rstrip("\n").split()])
    
    
    index = 0
    """Iterating through input_list """
    while index < len(total_list):
        node_count = int(total_list[index][0])

        """Generate a adjcency list from the given count of nodes"""
        adj_list = total_list[index: index + node_count + 1]
        root_index = int(adj_list[0][1])

        """Create an empty node"""
        tree = Tree(None)

        """traverse through the input adjcency matrix using depth first search and building a binary tree"""
        visited = [False] * len(adj_list[1])
        avl = DFS(root_index, adj_list[1:], visited, tree)

        """Find height and balance of binary tree"""
        print(get_height(avl) - 1, check_balanced_tree(avl))

        index = index + node_count + 1

main()