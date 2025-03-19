import java.io.*;
import java.util.*;

class Pair{
    int s;
    int e;
    Pair(int s, int e){
        this.s = s;
        this.e = e;
    }
}
public class Main {
    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> cards = new HashMap<Integer, Integer>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0;i<N;i++){
            int number = Integer.parseInt(st.nextToken());
            if(cards.containsKey(number)){
                cards.put(number, cards.get(number)+1);
            }
            else{
                cards.put(number, 1);
            }
        }
//        System.out.println(cards);
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 0;i < M; i++){
            int checkNum = Integer.parseInt(st.nextToken());
            int count = cards.getOrDefault(checkNum, 0);
            sb.append(count).append(" ");
        }
        System.out.println(sb);
    }
}
