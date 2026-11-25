class Solution(object):
    def uniqueOccurrences(self, arr):
        
        freq=[0]*2001
        for i in arr:
            freq[i+1000]+=1
        seenArr=[0]*1000
        for i in freq:
            if i>0:
              seenArr[i]+=1
              if seenArr[i]>1:
                return False
        return True
arr=[1,47,23,2,1,2,1,0]
print(uniqueOccurrences(arr))