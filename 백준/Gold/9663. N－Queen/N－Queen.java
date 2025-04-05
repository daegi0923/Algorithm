import java.io.*;
import java.util.*;


public class Main {
    static int N, ans;
    static boolean[] checkVertical;
    static boolean[] checkDiagonal1;
    static boolean[] checkDiagonal2;

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        checkVertical = new boolean[N];
        checkDiagonal1 = new boolean[2 * N - 1];
        checkDiagonal2 = new boolean[2 * N - 1];
        ans = 0;
        solve(0);
        System.out.println(ans);
//        for (int i = 0; i < N; i++) {
//            System.out.println();
//            for (int j = 0; j < N; j++) {
//                System.out.print(getDiagonal1(i, j) + " ");
//            }
//        }for (int i = 0; i < N; i++) {
//            System.out.println();
//            for (int j = 0; j < N; j++) {
//                System.out.print(getDiagonal2(i, j) + " ");
//            }
//        }
    }

    public static void solve(int row) {
//        System.out.println(startI + " " +startJ);
//        System.out.println(startI + " " + startJ + " " + count);
        if (row == N) {
            ans = ans + 1;
            return;
        }
        for (int col = 0; col < N; col++) {
            int diagNum1 = getDiagonal1(row, col);
            int diagNum2 = getDiagonal2(row, col);
//                System.out.println(diagNum1 + " " + diagNum2);
            if ( !checkVertical[col] && !checkDiagonal1[diagNum1] && !checkDiagonal2[diagNum2]) {
                checkVertical[col] = true;
                checkDiagonal1[diagNum1] = true;
                checkDiagonal2[diagNum2] = true;
                solve(row + 1);
                checkVertical[col] = false;
                checkDiagonal1[diagNum1] = false;
                checkDiagonal2[diagNum2] = false;


            }
        }

    }

    public static int getDiagonal1(int i, int j) {
        return i + j;
    }

    public static int getDiagonal2(int i, int j) {
        return i - j + N-1;
    }


}
