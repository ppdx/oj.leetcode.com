package oj.leetcode.com;

import java.util.*;


public class CombinationSumSolution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>(100);
        Stack<List<Integer>> listStack = new Stack<>();
        Stack<Integer> sumStack = new Stack<>();
        for (int n : candidates) {
            listStack.add(Collections.singletonList(n));
            sumStack.add(n);
        }
        while (!listStack.empty()) {
            List<Integer> list = listStack.pop();
            int sum = sumStack.pop();
            int i = Arrays.binarySearch(candidates, list.get(list.size() - 1));
            while (i < candidates.length && candidates[i] <= target - sum) {
                List<Integer> tmp = new ArrayList<>(list.size() + 1);
                tmp.addAll(list);
                tmp.add(candidates[i]);
                listStack.add(tmp);
                sumStack.add(sum + candidates[i]);
                i++;
            }
            if (sum == target)
                result.add(list);
        }
        return result;
    }

    public static void main(String[] args) {
        List<List<Integer>> result = new CombinationSumSolution().combinationSum(new int[]{2, 3, 6, 7}, 7);
        for (List<Integer> l : result) {
            System.out.print("[ ");
            for (int n : l) {
                System.out.print(n);
                System.out.print(" ");
            }
            System.out.println("]");
        }
        System.out.println("-----------------------------------");
        List<List<Integer>> result1 = new CombinationSumSolution().combinationSum(new int[]{1}, 2);
        for (List<Integer> l : result1) {
            System.out.print("[ ");
            for (int n : l) {
                System.out.print(n);
                System.out.print(" ");
            }
            System.out.println("]");
        }
    }
}
