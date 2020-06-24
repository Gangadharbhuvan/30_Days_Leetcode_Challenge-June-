'''
    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        
        pos_trees = [1, 1, 2]
        
        for i in range(3, n + 1):
            cur_comb = 0
            for j in range(i//2):
                cur_comb += 2*pos_trees[j]*pos_trees[i-j-1]
            if i % 2:
                cur_comb += pos_trees[i//2]*pos_trees[i//2]
            pos_trees.append(cur_comb)
        return pos_trees[-1]