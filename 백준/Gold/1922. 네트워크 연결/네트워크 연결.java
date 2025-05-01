import java.io.*;
import java.util.*;


class Edge{
    int start;
    int end;
    int cost;
    Edge(int start, int end, int cost){
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public String toString() {
        return this.start + " " + this.end + " "+ this.cost;

    }
}
public class Main {
    static int N, M;
    // N : 컴퓨터의 수, M : 선의 수
    static int[] parents;
    static void union(int a, int b){
        int rootA = find(a);
        int rootB = find(b);

        if(rootA != rootB){
            parents[rootB] = rootA;
        }
    }
    static int find(int x){
        if(parents[x] != x){
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }
    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        List<Edge> graph = new ArrayList<>();
        parents = new int[N+1];
        for(int i = 0; i < N+1; i++){
            parents[i] = i;
        }
        for(int i = 0;i < M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph.add(new Edge(start, end, cost));

        }
        graph.sort((a, b)->a.cost - b.cost);
//        System.out.println(graph);
        int root = graph.get(0).start;
//        parents[graph.get(0).end] = root;

        int cost = 0;
        for(Edge e : graph){
            if(find(e.start)!= find(e.end)){
                union(e.start, e.end);
                cost = cost + e.cost;
//                System.out.println(e.cost);
            }
        }
        System.out.println(cost);
    }
}
