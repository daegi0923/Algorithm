import java.io.*;
import java.util.*;
public class Main {
    static final int INF = 1000000;
    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        //dist 초기화
        int [][] dist = new int[N+1][N+1];
        for(int i = 1; i <= N; i++){
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            dist[A][B] = 1;
            dist[B][A] = 1;
        }
        for(int k = 1; k <= N; k++){
            for(int i = 1; i <= N; i++){
                for(int j = 1; j <= N; j++){
                    dist[i][j] = Math.min(dist[i][k] + dist[k][j], dist[i][j]);
                }
            }
        }
        int ans = -1;
        int minKevinBacon = Integer.MAX_VALUE;
        for(int i = 1; i <= N; i++){
            int sum = 0;
            for(int j = 1; j<=N;j++){
                sum = sum + dist[i][j];
            }
            if(sum < minKevinBacon){
                minKevinBacon = sum;
                ans = i;
            }
        }
        System.out.println(ans);
    }
}
