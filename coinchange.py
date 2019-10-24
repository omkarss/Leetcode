
def create_matrix(coin,amount):
    row_count = len(range(0,amount+1))
    

    return [[x for x in [0]*(amount+1)] for y in coin]


def coinchange(coin,amount):
    
    matrix = create_matrix(coin,amount)
    print(matrix)
    coin.sort()
    row = 0
    temp = 0
    
    for i in range(0,len(coin)):
        for j in range(amount+1):
            check = False
            if(j%coin[i] ==0 ):
                if(i == 0):
                    matrix[i][j] = int(j/coin[i])
                else:
                    if(matrix[i-1][j]>0):
                        matrix[i][j] = min(int(j/coin[i]) , matrix[i-1][j])
                    else:
                        matrix[i][j] = int(j/coin[i])
            else:
                if(i == 0 ):
                    matrix[i][j] = 0
                    continue

                k = 0
                res = j%coin[i]
                for k in range(j-1,-1,-1):
                    if(matrix[i][j-k]!=0):
                        check = True
                        temp = matrix[i][k] + matrix[i][j-k]
                        break
                
                if(check == True):
                    if(matrix[i-1][j]==0):
                        matrix[i][j] = matrix[i][k] + matrix[i][j-k]
                    else:
                        matrix[i][j] = min(matrix[i][k] + matrix[i][j-k],matrix[i-1][j])
            
                else:
                    matrix[i][j] = matrix[i-1][j]
    return(matrix[len(coin)-1][amount])






            




print(coinchange([1,3,4],10))