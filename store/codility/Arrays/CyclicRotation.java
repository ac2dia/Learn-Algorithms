// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.Arrays;
import java.util.stream.Stream;

class Solution {
    public int[] solution(int[] A, int K) {
        // write your code in Java SE 8
        if (A.length == 0) {
            return A;
        }

        int moveDistance = K % A.length;

        int[] leftArray = Arrays.copyOfRange(A, A.length-moveDistance, A.length);
        int[] rightArray = Arrays.copyOfRange(A, 0, A.length-moveDistance);

        int[] array = new int[A.length];
        System.arraycopy(leftArray, 0, array, 0, leftArray.length);
        System.arraycopy(rightArray, 0, array, leftArray.length, rightArray.length);

        return array;
    }
}