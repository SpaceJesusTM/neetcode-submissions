from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())

# Let n = number of strings, and m = average length of each string.
# Time: O(n * m), since we visit every character in every string once.
# Space: O(n * m) including the output groups that store all strings.
# The hash map keys use O(n * 26) in the worst case, which simplifies to O(n)
# because each key is a fixed-size 26-character frequency tuple.
