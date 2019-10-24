





def climbingsteps1or2(n):
    
    climber = [0]*(n+1)
    climber[0] = 1
    climber[1] = 1

    for i in range(2,n):
        climber[i] = climber[i-1] + climber[i-2]

    
    return(climber[n-1])

    


print(climbingsteps1or2(6))


