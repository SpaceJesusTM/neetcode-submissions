class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if x in num_dict.keys():
                return [num_dict[x], i]
            num_dict[nums[i]] = i         
        