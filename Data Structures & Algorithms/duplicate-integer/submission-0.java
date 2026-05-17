// import java.io.*;
// import java.util.*;
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable<Integer, Integer> dict = new Hashtable<Integer, Integer>();
         for (int i = 0; i < nums.length; i++) {
            if (dict.containsKey(nums[i]) == true) {
                return true;
            }
            dict.put(nums[i], i);
         }
        return false;
    }
}