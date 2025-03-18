import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int [][] grid = new int[N][3];
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int [] dpMax = Arrays.copyOf(grid[N-1], 3);
        int [] dpMin = Arrays.copyOf(grid[N-1], 3);
        int [] tempMin = new int[3];
        int [] tempMax = new int[3];
        for(int i = N-2; i > -1 ; i--){
            tempMax[0] = grid[i][0] + Math.max(dpMax[0], dpMax[1]);
            tempMax[1] = grid[i][1] + Math.max(Math.max(dpMax[0], dpMax[1]), dpMax[2]);
            tempMax[2] = grid[i][2] + Math.max(dpMax[1], dpMax[2]);
            tempMin[0] = grid[i][0] + Math.min(dpMin[0], dpMin[1]);
            tempMin[1] = grid[i][1] + Math.min(Math.min(dpMin[0], dpMin[1]), dpMin[2]);
            tempMin[2] = grid[i][2] + Math.min(dpMin[1], dpMin[2]);
            dpMax = tempMax.clone();
            dpMin = tempMin.clone();
        }
        int max = Math.max(dpMax[0], Math.max(dpMax[1], dpMax[2]));
        int min = Math.min(dpMin[0], Math.min(dpMin[1], dpMin[2]));
        System.out.println(max + " " + min);
    }
}
