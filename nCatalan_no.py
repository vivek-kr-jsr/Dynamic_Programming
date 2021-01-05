#https://practice.geeksforgeeks.org/problems/nth-catalan-number0817/1

def nc(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    M = 1000000007
    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
 
            # Calculate value using
            # previously stored values
            else:
                C[i][j] = (C[i-1][j-1] + C[i-1][j])
        
      
 
    return  C[n][k]
