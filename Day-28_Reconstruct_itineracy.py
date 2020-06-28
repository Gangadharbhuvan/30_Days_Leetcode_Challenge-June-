'''
    Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## RC ##
        ## APPROACH : GRAPH DFS ##
        ## EDGE CASE : [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
        
        def dfs(city):
            while(len(graph[city]) > 0):
                dfs(graph[city].pop(0))
            res.insert(0, city)                  # last airport
            
        graph = collections.defaultdict(list)
        for u, v in (tickets):
            graph[u].append(v)
            graph[u].sort()
        res=[]                
        dfs("JFK")
        return res
        