import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> holder = new Stack<Character> ();

        if (s.length() > 1) {
            for (int i=0; i<s.length(); i++) {
                boolean flag = false;
                if (holder.size() > 0) {
                    if (s.charAt(i) == ']') {
                        if (holder.peek() == '[') {
                            flag = true;
                        }
                    } 
                    else if (s.charAt(i) == '}'){
                        if (holder.peek() == '{') {
                            flag = true;
                        }
                    }
                    else if (s.charAt(i) == ')') {
                        if (holder.peek() == '(') {
                            flag = true;
                        } 
                    }
                }
                
                if (flag == false) {
                    holder.push(s.charAt(i));
                } else { holder.pop(); }
                
            }
        } else {return false; }

        if (holder.size() > 0) {
            return false;
        } else { return true; }
    }
}

class Main {
    public static void main(String[] args) {
        String s = "(])";
        Solution solution = new Solution();
        System.out.print(solution.isValid(s));
    }
}