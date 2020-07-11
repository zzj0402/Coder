class Solution:
    def reverse_check(self,s):
        index=len(s)-1
        temp=''
        while index>=0:
            temp+=s[index]
            index-=1
        return True if temp==s else False

    def longestPalindrome(self, s: str) -> str:
        result=''
        start=0
        length=1
        end=start+length+1
        while(start<len(s)):
            while (end<=len(s)):
                window=s[start:end]
                result=window if len(window)>len(result) and self.reverse_check(window) else result
                length+=1
            start+=1
        return result
