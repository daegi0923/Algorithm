import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int [][] item = new int[N+1][2];
        // [i][0] : item, [i][1] : value
        int [][] dp = new int[N+1][K+1];
        for(int i = 1; i < N+1; i++){
            st = new StringTokenizer(br.readLine());
            item[i][0] = Integer.parseInt(st.nextToken());
            item[i][1] = Integer.parseInt(st.nextToken());
        }
        for(int i = 1; i < N+1; i++){
            for(int w=1; w<K+1;w++){
                if(item[i][0] <= w){
                    dp[i][w] = Math.max(dp[i-1][w], dp[i-1][w- item[i][0]] + item[i][1]);
                }
                else{
                    dp[i][w] = dp[i-1][w];
                }
            }
        }

        System.out.println(dp[N][K]);
    }
}
