'''
    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



'''

class Solution(object):
    def numSquares(self, n):
        from math import ceil, sqrt
        dp = [0, 1, 2, 3]
        if n<=3:
            return dp[n]
        else:
            for i in range(4, n + 1):
                dp.append(i)
                for x in range(1, int(ceil(sqrt(i))) + 1):
                    temp = x*x
                    if temp>i:
                        break
                    else:
                        dp[i] = min(dp[i], 1 + dp[i - temp])
        return dp[n]