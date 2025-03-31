import java.io.*;
import java.util.*;


public class Main {
    static char[][] stars;
    static char star = '*';

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        stars = new char[N][N * 2 - 1];
        for (int i = 0; i < N; i++) {
            Arrays.fill(stars[i], ' ');
        }
        drawTriangle(0, N - 1, N);
        for (int i = 0; i < N; i++) {
            System.out.println(new String(stars[i]));
        }
    }

    static void drawTriangle(int x, int y, int size) {
        if (size == 3) {
            stars[x][y] = star;
            stars[x + 1][y - 1] = star;
            stars[x + 1][y + 1] = star;
            for (int i = -2; i <= 2; i++) {
                stars[x + 2][y + i] = star;
            }
            return;
        }
        int half = size/2;
        drawTriangle(x, y, half);
        drawTriangle(x+half, y-half, half);
        drawTriangle(x+half, y+half, half);
    }
}
