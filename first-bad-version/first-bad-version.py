# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l, h = 1, n
        badVersion = n
        
        while(l<=h):
            mid = (l+h) //2
            
            if(isBadVersion(mid)):
                h = mid-1
                badVersion = mid
            else:
                l = mid+1
            
        return badVersion
                