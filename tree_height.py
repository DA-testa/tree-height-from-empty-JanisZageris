# python3

import sys
import threading
import numpy
import os

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

def build_tree(n, parents):
    nodes = [Node() for _ in range(n)]
    root = None
    for i, p in enumerate(parents):
        if p == -1:
            root = nodes[i]
        else:
            nodes[p].children.append(nodes[i])
            nodes[i].parent = nodes[p]
    return root

def compute_height(node):
    if not node.children:
        return 0
    heights = [compute_height(child) for child in node.children]
    return 1 + max(heights)

def main():
    mode = input()
    
    file_name = input()
    file_path = os.path.join("test", file_name)
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        parents = list(map(int, file.readline().strip().split()))
    
    tree = build_tree(n, parents)
    height = compute_height(tree) + 1
    print(height)

sys.setrecursionlimit(10**7)  # max depth of recursion
main()
