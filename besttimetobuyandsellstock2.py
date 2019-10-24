def maxprofit(prices):
    sum = 0
        
    for i in range(0,len(prices)-1):
        if(prices[i]<prices[i+1]):
            sum = sum + (prices[i+1]-prices[i])
    return sum


print(maxprofit([7,9]))