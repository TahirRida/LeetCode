class Solution {
    public String longestCommonPrefix(String[] strs) {
        String commonPrefix="";
        char charAtthisIndex=0;
        int shortestStringLength=strs[0].length();
        //determining the length of the shortest string in the table.
        for(int i=1;i<strs.length;i++){
            if(strs[i].length()<shortestStringLength){
                shortestStringLength=strs[i].length();
            }
        }
        //Now comparing each character of the strings,but only the parts of which the length<shortestStringLength
        for (int j=0;j<shortestStringLength;j++){
            boolean charIsInCommonPrefix=true;
            charAtthisIndex=strs[0].charAt(j);
            for(int i=1;i<strs.length;i++){
                if(strs[i].charAt(j) != charAtthisIndex){
                    charIsInCommonPrefix = false;
                }
            }
            if(charIsInCommonPrefix){
                commonPrefix+=charAtthisIndex;
            }
            else{
                return commonPrefix;
            }
        }
        return commonPrefix;
    }
}