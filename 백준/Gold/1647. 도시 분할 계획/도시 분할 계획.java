import java.io.*;
import java.util.*;


class Edge {
    int start;
    int end;
    int dist;

    Edge(int start, int end, int dist) {
        this.start = start;
        this.end = end;
        this.dist = dist;
    }

}

public class Main {
    static int N, M;
    static List<Edge> edgeList = new ArrayList<>();
    static int[] parent;
    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        parent = new int[N+1];
        for(int i = 0; i <N ; i++){
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            edgeList.add(new Edge(start, end, dist));
        }
        edgeList.sort((a, b) -> {
            return a.dist - b.dist;
        });
        int cnt = 0;
        int sumCost = 0;
        for(int i = 0;i< M; i++){
            if(N == 2) break;
            Edge e = edgeList.get(i);
            if(find(e.start) != find(e.end)){
                union(e.start, e.end);
                cnt = cnt + 1;
                sumCost = sumCost + e.dist;
                if(cnt == N-2) break;
            }
        }
        System.out.println(sumCost);
    }
    public static int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    public static void union(int a, int b ){
        int rootA = find(a);
        int rootB = find(b);
        if(rootA != rootB){
            parent[rootB] = rootA;
        }
    }

}
