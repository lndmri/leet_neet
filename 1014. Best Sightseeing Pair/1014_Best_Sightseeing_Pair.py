# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

 

# Example 1:

# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# Example 2:

# Input: values = [1,2]
# Output: 2
 

# Constraints:

# 2 <= values.length <= 5 * 104
# 1 <= values[i] <= 1000


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_i = 0
        max_score = 0

        for i, j in zip(range(0, len(values) - 1), range(1, len(values))):
            if values[i] + i > max_i:
                max_i = values[i] + i
            
            score = max_i + values[j] - j
            max_score = max(max_score, score)
    
        return max_score




        # trivial solution (O N^2) Causes TLE
        score = 0
        max_score = 0

        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                score = values[i] + i + values[j] - j
                max_score = max(max_score, score)
            
        return max_score