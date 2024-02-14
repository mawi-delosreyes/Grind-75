import java.util.HashSet;

class Solution {
    public boolean isPalindrome(String s) {
        
        int start = 0, end = s.length()-1;

        while (start < end) {

            if (!Character.isLetterOrDigit(s.charAt(start))) {
                start += 1;
            } 
            else if (!Character.isLetterOrDigit(s.charAt(end))) {
                end -= 1;
            } else {
                if (Character.toLowerCase(s.charAt(start)) != Character.toLowerCase(s.charAt(end))) {
                    return false;
                }
                start += 1;
                end -= 1;
            }
        }
        return true;
    }
}

class Main {
    public static void main(String[] args) {
        String s = "aa";
        Solution solution = new Solution();
        System.out.print(solution.isPalindrome(s));
    }
}