class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}
        
        for idx, n in enumerate(nums):
            currentSum = target - n
            if currentSum in bag:
                return [bag[currentSum], idx]
            bag[n] = idx
        return 
        
#Time Complexity: O(n)
#Space Complexity: O(n)