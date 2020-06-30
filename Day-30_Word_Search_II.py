'''
        Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
   Hide Hint #1  
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
   Hide Hint #2  
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.




'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie ={}
        for word in words:
            cTrie = trie
            for c in word:
                if not c in cTrie:
                    cTrie[c] = {}
                cTrie = cTrie[c]
            cTrie['$']=word

        neighbors = [[0,1],[1,0],[-1,0],[0,-1] ]
        out = set()
        def explore(x,y,trie):
            if   x <0 or y <0 or x >= len(board)  or y >=len(board[0]):return
            c = board[x][y]
            if c  in trie :
                trie = trie[c]
                if '$' in trie:
                    out.add(trie['$'])
                    
                board[x][y]='#'
                for nx,ny in neighbors:
                    explore(x+nx,y+ny,trie)
                board[x][y]=c

        for i in range(len(board)):
            for j in range(len(board[0])): explore(i,j,trie)
        return out 