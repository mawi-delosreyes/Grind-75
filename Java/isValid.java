import java.util.ArrayList;

class Solution {
    public boolean isValid(String s) {

        ArrayList<Character> holder = new ArrayList<Character> ();

        if (s.length() > 1) {
            for  (int i = 0; i < s.length(); i++) {

                if (s.charAt(i) == '}' && holder.size() > 0 && holder.get(holder.size()-1) == '{') {
                    holder.remove(holder.size()-1);
                } else if (s.charAt(i) == ']' && holder.size() > 0 && holder.get(holder.size()-1) == '[') {
                    holder.remove(holder.size()-1);
                } else if (s.charAt(i) == ')' && holder.size() > 0 && holder.get(holder.size()-1) == '(') {
                    holder.remove(holder.size()-1);
                } else {
                    holder.add(s.charAt(i));
                }
            }
        } else { return false; }
        
        if (holder.size() > 0) { 
            return false;
        } else { return true;}

    }
}

class Main {
    public static void main(String[] args) {
        String s = "){";
        Solution solution = new Solution();
        System.out.print(solution.isValid(s));
    }
}