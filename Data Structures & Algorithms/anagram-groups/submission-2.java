class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];

            // In Java, characters can be subtracted directly.
            // c - 'a' maps lowercase letters to indices:
            // 'a' -> 0, 'b' -> 1, ..., 'z' -> 25.
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            // Convert the count array into a String so it can be used as a HashMap key.
            // Example: [1, 0, 0, ..., 1, ..., 1] for "eat", "tea", and "ate".
            String key = Arrays.toString(count);

            if (!groups.containsKey(key)) {
                groups.put(key, new ArrayList<>());
            }

            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}