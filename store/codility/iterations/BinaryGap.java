// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.List;
import java.util.ArrayList;

class Solution {
    public int solution(int N) {
        int max_gap = 0;

        String binaryString = Integer.toBinaryString(N);

        List<Integer> indexList = findIndexes("1", binaryString);
        for (int i=1; i < indexList.size(); i++) {
            if (max_gap < indexList.get(i) - indexList.get(i-1) - 1) {
                max_gap = indexList.get(i) - indexList.get(i-1) - 1;
            }
        }

        return max_gap;
    }

    public List<Integer> findIndexes(String word, String document) {

        List<Integer> indexList = new ArrayList<Integer>();
        int index = document.indexOf(word);

        while(index != -1) {
            indexList.add(index);
            index = document.indexOf(word, index+word.length());
        }

        return indexList;
    }
}