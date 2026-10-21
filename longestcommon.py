class Solution:
    def longestCommon(self,str):
        prefix=str[0]
        for s in str[1:]:
            for i in range(len(prefix)):
                if i>=len(s) or prefix[i]!=s[i]:

                    prefix=prefix[:i]
                    break
            git return prefix
str=["flower","flow","fly","flight"]
obj=Solution()
print(obj.longestCommon(str))

