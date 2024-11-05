class Solution {
    public int countGoodSubstrings(String s) {
        if(s.length()<2){
            return 0 ;
        }
        int goodStrings = 0;
        int low = 0;
        int high = 2;
        while(high < s.length()){
            char a = s.charAt(low);
            char b = s.charAt(low+1);
            char c = s.charAt(high);
            if(a==b || b == c || a == c){
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