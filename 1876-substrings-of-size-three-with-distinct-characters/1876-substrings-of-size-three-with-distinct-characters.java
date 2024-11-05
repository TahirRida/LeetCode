class Solution {
    public int countGoodSubstrings(String s) {
        if(s.length()<2){
            return 0 ;
        }
        int goodStrings = 0;
        int low = 0;
        int high = 2;
        while(high < s.length()){
            if(s.charAt(low) == s.charAt(low +1) || s.charAt(low+1) == s.charAt(high) || s.charAt(low) == s.charAt(high)){
                low++;
                high++;
                continue;
            }
            goodStrings++;
            low++;
            high++;
        }
        return goodStrings;
    }
}