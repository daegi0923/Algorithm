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
        List<Pair> times = new ArrayList<>();
        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            times.add(new Pair(s, e));
        }
        Collections.sort(times, (e1, e2) -> {
            if (e1.e == e2.e) {  // 시작 시간이 같다면 종료 시간 기준 정렬
                return e1.s - e2.s;
            }
            return e1.e - e2.e;  // 시작 시간 기준 정렬
        });
        int count = 0;
        int lastEndTime = 0;
        for(Pair meeting : times){
            if(meeting.s >= lastEndTime){
                count = count + 1;
                lastEndTime = meeting.e;
            }
        }
        System.out.println(count);
    }
}
