





def maxProfit(stockprice):
    max_diff = float("inf")
    i = 0
    max_profit = 0
    min_val = stockprice[0]
    
    while(i<len(stockprice)):
        if(stockprice[i] < min_val):
            min_val = stockprice[i]

        if(stockprice[i]- min_val > max_profit):
            max_profit = stockprice[i]- min_val
        
        i = i + 1
    
    return max_profit
        



        

        #temp.append(stockprice[len(stockprice)]-stockprice[len(stockprice)-2])

    

#print('Hey')


print(maxProfit([4,1,4,9,0]))