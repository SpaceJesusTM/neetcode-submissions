class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

# Time: O(n), because we scan the list once.
# Space: O(n), because in the worst case we store every number in the hash map.