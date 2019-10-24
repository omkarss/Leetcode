# Leetcode Best time to buy and sell stock 
import math

def maxProfit( prices):
    max = 0
    

    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):
            if((prices[j] - prices[i])>max):
                max = prices[j] - prices[i]
            
    return(max)







print(maxProfit([2,4,1]))
        