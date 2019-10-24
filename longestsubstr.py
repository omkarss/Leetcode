def search(element, temp_arr):
    for i in range(0,len(temp_arr)):
        if temp_arr[i] == element:
            return i

    return -1




def remove_element(temp_arr, index):

    for i in range(0,index):
        temp_arr.pop(0)
    return temp_arr


class Solution:
    def lengthOfLongestSubstring(self, s):
        if(s == None):
            return 0
        MAX = 0
        count = 0
        temp_arr = []
        for i in range(0,len(s)):
            if(s[i] in temp_arr):
                index = search(s[i],temp_arr)
                temp_arr = remove_element(temp_arr,index+1)
                temp_arr.append(s[i])
                count = len(temp_arr)
                #temp_arr.append(s[i])
            else:
                temp_arr.append(s[i])
                count = count + 1

            if(MAX<count):
                MAX = count
        return MAX





s=Solution()
print(s.lengthOfLongestSubstring('vabcbqwert'))
