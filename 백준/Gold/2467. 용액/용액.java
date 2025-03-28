import java.io.*;
import java.util.*;


public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[] values = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            values[i] = Integer.parseInt(st.nextToken());
        }
        int minValue = Integer.MAX_VALUE;
        int ansRight = N-1;
        int ansLeft = 0;
        Arrays.sort(values);
        int left = 0;
        int right = N - 1;
        while (left < right) {
            int localAns = values[right] + values[left];
            if (Math.abs(localAns) < minValue) {
                minValue = Math.abs(localAns);
                ansRight = values[right];
                ansLeft = values[left];
            }
            if (localAns <= 0) {
                left = left + 1;
            } else if (localAns > 0) {
                right = right - 1;
            } else {
                break;
            }
        }
        System.out.println(ansLeft + " " + ansRight);

    }

}
