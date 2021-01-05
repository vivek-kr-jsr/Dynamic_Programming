#https://practice.geeksforgeeks.org/problems/coin-change2448/1
def count(self, S, m, n): 
        # code here 
        t = [[0 for x in range(m)] for x in range(n+1)]
        for i in range(m):
            t[0][i]=1
        for i in range(1, n+1): 
            for j in range(m): 
  
            # Count of solutions including S[j] 
                
                x = t[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
                y = t[i][j-1] if j >= 1 else 0
  
            # total count 
                t[i][j] = x + y 
  
        return t[n][m-1] 
