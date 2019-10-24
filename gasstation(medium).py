def canCompleteCircuit(gas,cost):
    max_val= 0
    s_index = 0
    gas_suff = False
    
    if(len(gas)==1):
        return gas[0]





    while(True):
        if((i+1)%len(gas)== s_index):
            if(gas_sum-cost[i%len(gas)] < 0):
                return -1
            else:
                return s_index
        
        else:
            if(gas_sum-cost[i]<0):
                return -1
            else:

                gas_sum = gas_sum - cost[i] + gas[(i+1)%len(gas)]
            
        i = (i + 1)%len(gas)


#print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(canCompleteCircuit([5,8,2,8],[6,5,6,6]))







    
