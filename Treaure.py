#Medium Level



MAX = 10000

def findminway(arr,m,n):

    count_arr = [[MAX for i in range(0,len(arr[0])+2)] for j in range(0,len(arr)+2)]
    print(count_arr)
    count_arr[1][1] = 0

    for i in range(1, len(arr)+1):
        for j in range(1, len(arr[0])+1):
            if(i == 1  and j == 1):
                continue
            if((i>len(arr) or j > len(arr[0])) ):
                count_arr[i][j] = MAX
            if(arr[i-1][j-1] == 'D'):
                count_arr[i][j]=MAX
            else:
                count_arr[i][j] = 1+min(count_arr[i][j-1], count_arr[i][j+1], count_arr[i-1][j],count_arr[i+1][j])

    count_arr[m][n] = 1 + min(count_arr[m][n-1], count_arr[m][n+1], count_arr[m-1][n],count_arr[m+1][n])


    return count_arr[m][n]


print(findminway([['O','O','O'],['O','D','O'],['O','D','X']],3,3))