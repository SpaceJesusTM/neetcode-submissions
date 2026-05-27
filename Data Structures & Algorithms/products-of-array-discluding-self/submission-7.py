class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1

        for num in nums:
            product *= num
            prefix.append(product)

        suffix = []
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            suffix.append(product)

        suffix.reverse()

        result = []

        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < len(nums) - 1 else 1
            result.append(left * right)

        return result