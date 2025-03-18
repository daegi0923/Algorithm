import java.io.*;
import java.util.*;


class Pair{
    int x;
    int y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}
public class Main {
    public static int N;
    public static int M;
    public static int[][] board;
    public static int[][] visited;
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {1, -1, 0, 0};


    public static void BFS(int i, int j){
        Queue<Pair> queue = new LinkedList<>();
        visited[i][j] = 0;
        queue.add(new Pair(i, j));
        while(!queue.isEmpty()){
            Pair here = queue.poll();
            int hereX = here.x;
            int hereY = here.y;
            for(int d = 0; d<4;d++){
                int nextX = hereX + dx[d];
                int nextY = hereY + dy[d];
                if(0<=nextX && nextX <N && 0<=nextY && nextY<M &&
                board[nextX][nextY]==1 && visited[nextX][nextY] == 0){
                    visited[nextX][nextY] = visited[hereX][hereY] + 1;
                    queue.add(new Pair(nextX, nextY));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visited = new int[N][M];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0;j<M;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        br.close();
//        System.out.println(N+" "+M);
        int startI = 0;
        int startJ = 0;

        for(int i = 0; i < N; i ++){
            for(int j = 0;j<M;j++){
                if(board[i][j]==2){
                    startI = i;
                    startJ = j;
                    break;
                }
            }
        }
        BFS(startI, startJ);
        for(int i = 0; i<N;i++){
            for(int j = 0;j<M;j++){
                if(board[i][j] == 1 && visited[i][j] == 0){
                    visited[i][j] = -1;
                }
            }
        }
        for(int []line:visited){
            for(int e:line){
                System.out.print(e + " ");
            }
            System.out.println();
        }
    }
}
