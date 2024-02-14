import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> s_holder = new HashMap<Character, Integer>();
        HashMap<Character, Integer> t_holder = new HashMap<Character, Integer>();
        Character s_key, t_key;

        if (s.length() != t.length()) {
            return false;
        }

        for (int i=0; i<s.length(); i++) {
            s_key = Character.toLowerCase(s.charAt(i));
            t_key = Character.toLowerCase(t.charAt(i));

            if (s_holder.containsKey(s_key)) {
                s_holder.put(s_key, s_holder.get(s_key) + 1);
            } else { s_holder.put(s_key, 1);}

            if (t_holder.containsKey(t_key)) {
                t_holder.put(t_key, t_holder.get(t_key) + 1);
            } else { t_holder.put(t_key, 1); }
        }

        return s_holder.equals(t_holder);
    }
}

class Main {
    public static void main(String[] args) {
        String s = "aa";
        String t = "bb";
        Solution solution = new Solution();
        System.out.print(solution.isAnagram(s, t));
    }
}