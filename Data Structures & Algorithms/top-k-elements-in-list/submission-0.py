class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create buckets where index = frequency
        # We use len(nums) + 1 because a number can appear len(nums) times.
        # buckets[0] is unused, but it keeps the indexing simple.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put each number into the bucket matching its frequency
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 4: Scan from highest frequency to lowest frequency
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res