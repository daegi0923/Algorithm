import java.io.*;
import java.util.*;

class Edge {
    int start;
    int end;
    int cost;

    Edge(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public String toString() {
        return this.start + " " + this.end + " " + this.cost;
    }
}


public class Main {
    static int V, E;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        parent = new int[V + 1];
        for (int i = 1; i < V + 1; i++) {
            parent[i] = i;
        }
        List<Edge> edgeList = new ArrayList<>();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            edgeList.add(new Edge(start, end, cost));

        }
        edgeList.sort((a, b) -> a.cost - b.cost);

        int cnt = 0;
        int sumCost = 0;
        for (Edge e : edgeList) {
            if (find(e.start) != find(e.end)) {
                union(e.start, e.end);
                sumCost = sumCost + e.cost;
                cnt = cnt + 1;
                if (cnt == V - 1) break;
            }

        }
        System.out.println(sumCost);
    }

    static int find(int x) {
//        System.out.println(parent[x] + " " + x);
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
//        System.out.println("union : "+a + b + rootA+" "+ rootB);
        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }

}
