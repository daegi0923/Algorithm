import java.io.*;
import java.util.*;

public class Main {
    public static int N;

    public static int C;
    public static int[] houses;
    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        houses = new int[N];

        for(int i =0;i<N;i++){
            houses[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(houses);
        int left = 0;
        int right = houses[N-1] - houses[0];
        int ans =0;
        while(left <= right){
            int mid = (left + right)/2;
            if(canInstall(mid)){
                ans = mid;
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        System.out.println(ans);
    }
    public static boolean canInstall(int dist){
        int count = 1;
        int lastHouse = houses[0];
        for(int i=0;i<N;i++){
            if(houses[i]-lastHouse >= dist){
                count = count + 1;
                lastHouse = houses[i];
            }
        }
        return count >= C;
    }
}
