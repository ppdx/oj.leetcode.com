package oj.leetcode.com;

public class LengthOfLastWordSolution {
    public int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        if (words.length != 0)
            return words[words.length - 1].length();
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(new LengthOfLastWordSolution().lengthOfLastWord("hello world"));
    }
}
