
def buddyStrings(A, B):
    if len(A)!=len(B):
        return False
    else:
        all_same = True
        count = 0
        diff_arr = []
        for i in range(len(A)):
            if(i>=1):
                if(A[i] != A[i-1]):
                    all_same = False

            if(A[i] == B[i]):
                continue
            else:
                diff_arr.append(i)
                count = count + 1

        if(count == 0 and all_same == True):
            return True

        if(count == 0 and all_same ==False):
            if(sorted(A) == sorted(B)):
                return True
            else:
                return False

        if(count == 2):
        
            if(A[diff_arr[0]] == B[diff_arr[1]] and A[diff_arr[1]] == B[diff_arr[0]]):
                return True
        
        else:
            return False

        





print(buddyStrings('abab','abab'))


