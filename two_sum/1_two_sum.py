# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Best solution: just one pass
        prevMap = {} #num:index

        # for each number in the list and its enumeration
        for i, num in enumerate(nums):
            diff = target - num # we want to know if the diff is in the map already
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[num] = i    # if it is not in the map we then add the num and its index to the map


        # Second best solution: two passes over the list
       
        # # We will keep a dictionary with the differences of each eleement in the array
        # differences = dict()
        
        # # First pass to populate the dictionary
        # for i, num in enumerate(nums):
        #     differences[target - num] = i

        # print(differences)

        # # Second pass to get the solution.
        # for i in range(len(nums)):
        #     sol = differences.get(nums[i])
        #     if sol != None and sol != i:
        #         return [i, sol]


        # naive solution 
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums [j] == target:
        #             return [i,j]