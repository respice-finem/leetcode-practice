class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    """
    Two Pass
    Time Complexity: O(n + m)
    Space Complexity: O(n)

    TODO:
    1. We do a BFS and create an clone mapping. We then append the neighbors if they are already available in the map. Otherwise create and map if they are not already neighbors
    """
    if not node:
        return node
    if not node.neighbors:
        return Node(node.val)

    node_mapping = {}
    queue = deque()
    queue.append(node)
    seen = set()

    while queue:
        curr_node = queue.popleft()
        seen.add(curr_node)
        if curr_node not in node_mapping:
            node_mapping[curr_node] = Node(curr_node.val)
        for neighbor in curr_node.neighbors:
            if neighbor not in node_mapping:
                node_mapping[neighbor] = Node(neighbor.val)
            if node_mapping[neighbor] not in node_mapping[curr_node].neighbors:
                node_mapping[curr_node].neighbors.append(node_mapping[neighbor])
            if neighbor not in seen:
                queue.append(neighbor)

    return node_mapping[node]