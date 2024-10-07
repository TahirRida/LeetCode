class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        int a = s.length()-1;
        int i =0;
        while(i<=a){
            if(!(Character.isAlphabetic(s.charAt(i)) ||('0'<=s.charAt(i) && s.charAt(i)<='9'))){
                i++;
                continue;
            }
            if(!(Character.isAlphabetic(s.charAt(a)) ||('0'<=s.charAt(a) && s.charAt(a)<='9'))){
                a--;
                continue;
            }
            if (s.charAt(a)!= s.charAt(i)){
                return false;
            }
            i++;a--;
        }
        return true;
    }
}
