#https://practice.geeksforgeeks.org/viewSol.php?subId=8aacaf36e9cfaf4fa35de65429bce4fc&pid=701431&user=vivek29rajput

def knapSack(W,wt,val,n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Base Condition
    for i in range(n+1):
        for j in range(W+1):
            
            if i==0 or j==0:
                K[i][j]=0
    # if the weight of knapsack is more then the 
    # capacity of bag then the item not included 
    # in the bag
    
   
            elif (wt[i-1] > j):
                K[i][j]= K[i-1][j]
    
            else:
                K[i][j] =max(
                    val[i-1] + 
                    K[i-1][j-wt[i-1]],K[i-1][j])
    return K[n][W]

    

    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        print(knapSack(W,wt,val,n))
