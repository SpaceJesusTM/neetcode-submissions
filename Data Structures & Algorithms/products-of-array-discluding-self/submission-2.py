class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for num in nums:
            product = product * num
            prefix.append(product)
            
        suffix = []
        product = 1
        for i in range (len(nums) - 1, -1, -1):
            product = product * nums[i]
            suffix.append(product)
        
        suffix.reverse()

        result = []
        result.append(suffix[1])
        for i in range(1, len(nums) - 1):
            product = prefix[i - 1] * suffix[i + 1]
            result.append(product)

        result.append(prefix[len(nums) - 2])

        return result

        