class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newNums = set() 
        
        for n in nums:
            if n in newNums:
                return True
            else:
                newNums.add(n)
                
        return False
        
#Time Complexity: O(n)
#Space Complexity: O(n)