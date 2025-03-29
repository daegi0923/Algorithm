import java.io.*;
import java.util.*;


public class Main {
    static String[] board;
    static boolean[][] visited;
    static int R, C, ans;
    static int[] di = {0, 0, 1, -1};
    static int[] dj = {1, -1, 0, 0};
    static boolean[] alphaVisited = new boolean[26];

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        visited = new boolean[R][C];
        board = new String[R];
        for (int i = 0; i < R; i++) {
            board[i] = br.readLine();
        }
//        System.out.println((int)'A');
//        System.out.println(Character.getNumericValue('a'));
        visited[0][0] = true;
        alphaVisited[getInteger(board[0].charAt(0))] = true;
        dfs(0, 0, 1);
        System.out.println(ans);
    }

    public static void dfs(int ci, int cj, int length) {
//        System.out.println(board[ci].charAt(cj));
        if (ans < length) ans = length;
        for (int d = 0; d < 4; d++) {
            int ni = ci + di[d];
            int nj = cj + dj[d];
            if (ni < 0 || R <= ni || nj < 0 || C <= nj) continue;
            int alpha = getInteger(board[ni].charAt(nj));
            if (!visited[ni][nj] && !alphaVisited[alpha]) {
                visited[ni][nj] = true;
                alphaVisited[alpha] = true;
                dfs(ni, nj, length + 1);
                alphaVisited[alpha] = false;
                visited[ni][nj] = false;
            }
        }
    }


    public static int getInteger(char c) {
        return (int) c - (int) 'A';

    }

}

