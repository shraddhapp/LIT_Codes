class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length() == 0){
            return 0;
        }
        //windows sliding 
        int end = 0;
        int i =0;
        while( i< haystack.length() && end < needle.length()){
            if(haystack.charAt(i) == needle.charAt(end)){
                end++;
                if(end == needle.length()){
                    return i - end +1;
                }
                i++;
            }
            else{
                i = i - end+1;
                end = 0;
            }
        }
        return -1;
    }
}