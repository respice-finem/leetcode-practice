def validTree(n: int, edges: List[List[int]]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    NOTE:
    Key concepts here is that for a valid tree to exists
    - Only one connected component, any node will be able to reach all other nodes. We want to prevent any cycles in the case where the second condition is allowed
    - Number of edges is number of nodes - 1

    TODO:
    1. We build the adjacency matrix of the graph
    2. We then do a DFS. Few things to take note about the DFS is that we have to be sure that the previous node will not be revisited, i.e. the node which it came from. If any node is already visited we return False
    3. Else we return True
    """
    # Check if number of edges is number of nodes - 1
    if len(edges) != n - 1:  # Important property to learn
        return False

    # Build adjacency matrix for DFS
    adj_matrix = {i: set() for i in range(n)}
    for source, dest in edges:
        adj_matrix[source].add(dest)
        adj_matrix[dest].add(source)

    # Handle remaining edge cases of cycles existing while first condition exists
    seen = set()
    def dfs(start):
        if start in seen:
            return
        seen.add(start)
        for neighbors in adj_matrix[start]:
            dfs(neighbors)
    dfs(0)
    return len(seen) == n

    """
    Time Complexity: O(n * alpha(n))
    Space Complexity: O(n)
    --> Answer from editorial
    NOTE: Union Find

    TODO:
    1. We utilize union find to instead of DFS since this would require us to build the adjacency adj_matrix
    2. Union find builds on the idea of merging two sets of nodes under a single parent. This would be represented as an array of nodes with the parents as the value for this implementation
    3. The goal is to make sure that we do not find any sets that were previously merged as ideally we would want to combine all the sets. If there were sets that were already generated, this would mean a cycle has occurred. 
    """
    if len(edges) != n - 1:
        return False

    # unionFind = NaiveUnionFind(n)
    unionFind = UnionFind(n)
    for A, B in edges:
        if not unionFind.union(A, B):
            return False
    print(unionFind.parent)
    print(unionFind.size)
    return True
        
class NaiveUnionFind:

    def __init__(self, n):
        self.parent = [node for node in range(n)]

    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:  # This means that it has already been merged into the same set
            return False
        self.parent[root_A] = root_B
        return True

class UnionFind:

    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]

        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        
        return root

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False
        
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True
