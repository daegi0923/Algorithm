import java.io.*;
import java.util.*;

public class Main {
    public static int findYear(int M, int N, int x, int y) {
        int max = lcm(M, N); // 카잉 달력의 마지막 해
        for (int k = x; k <= max; k += M) {
            // k는 x ≡ k mod M 을 만족
            if ((k - 1) % N + 1 == y) {
                return k;
            }
        }
        return -1;
    }

    // 최소공배수
    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    // 최대공약수 (유클리드 호제법)
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            System.out.println(findYear(M, N, x, y));
        }
    }
}
