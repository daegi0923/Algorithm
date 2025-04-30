import java.io.*;
import java.util.*;

public class Main {
    static int solve(int N, int r, int c, int ans) {
        if (N == 1) {
//            System.out.println(ans + " " + r + "  " + c);
            return ans + r * 2 + c;
        }
        int len = (int) Math.pow(2, N);
        int block = (int) Math.pow(2, 2 * N - 2);
        if (r < len / 2) {
            if (c < len / 2) {

            } else {
                ans = ans + block;
            }
        } else {
            if (c < len / 2) {
                ans = ans + 2 * block;
            } else {
                ans = ans + 3 * block;
            }
        }
        return solve(N - 1, r %(int) Math.pow(2, N-1), c % (int) Math.pow(2, N-1), ans);
    }

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        int N, r, c;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        int res = solve(N, r, c, 0);
        System.out.println(res);
    }
}
