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
    public static boolean[][]visited;
    public static int[][] board;
    public static int N;
    public static List<Integer> groupCounts;
    public static int[]dx = {1, -1, 0, 0};
    public static int[]dy = {0, 0, 1, -1};

    public static void BFS(int i, int j){
        if(visited[i][j]){
            return;
        }
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(i, j));
        visited[i][j] = true;
        int count = 1;
        while(!queue.isEmpty()){
            Pair here = queue.poll();
            int hereX = here.x;
            int hereY = here.y;
//            System.out.println(hereX + " " + hereY);

            for(int d = 0; d < 4; d++){
                int nextX = hereX + dx[d];
                int nextY = hereY + dy[d];
                if(0<=nextX && nextX<N && 0<=nextY && nextY <N &&
                        board[nextX][nextY] == 1 && !visited[nextX][nextY]){
                    queue.add(new Pair(nextX, nextY));
                    visited[nextX][nextY] = true;
                    count = count + 1;
                }
            }
        }
        groupCounts.add(count);
    }

    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        //board, visited, groupCounts 초기화
        board = new int[N][N];
        visited = new boolean[N][N];
        groupCounts = new ArrayList<>();
        //board 입력 받기
        for(int i = 0; i<N;i++){
            String line = br.readLine();
            for(int j = 0; j<N;j++){
                board[i][j] = line.charAt(j)-'0';
            }
        }
//        for(int [] line : board){
//            System.out.println();
//            for(int e:line){
//                System.out.print(e);
//            }
//        }
//        for(boolean [] line : visited){
//            System.out.println();
//            for(boolean e:line){
//                System.out.print(e);
//            }
//        }

        //i, j 가 방문처리되지 않았으면, BFS 실행
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] == 1 && !visited[i][j]){
                    BFS(i, j);
                }
            }
        }
        Collections.sort(groupCounts);
        System.out.println(groupCounts.toArray().length);
        groupCounts.stream().forEach(e-> System.out.println(e));
    }
}
