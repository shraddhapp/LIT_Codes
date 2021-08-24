class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertPos = m + n - 1   #Length of merged array
        m, n = m-1, n-1 #Last index of both the array

        while m>=0 or n>=0:
            #As the list is sorted, compare from last and and put the grater element at insertpos
            
            print("---------\nm={0}, n={1}, IP={2}".format(m,n,insertPos))
            
            if(m<0 or n<0):
                if (m<0):
                    print("m loop")
                    nums1[insertPos] = nums2[n]
                    n -= 1
                else:
                    print("\n nloop IP={0}, m={1}".format(insertPos,m))
                    nums1[insertPos] = nums1[m]
                    m-= 1
                
            elif nums1[m] > nums2[n]:
                nums1[insertPos] = nums1[m]
                m -= 1 #Move the pointer to next larger
            else:
                nums1[insertPos] = nums2[n]
                n -= 1
            
            print(nums1)
            insertPos -= 1          