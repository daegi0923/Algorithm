import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

class Node {
    int index;
    int dist;

    public Node(int index, int dist) {
        this.index = index;
        this.dist = dist;
    }

}

class Edge {
    int dist;
    int nextNode;

    public Edge(int nextNode, int dist) {
        this.dist = dist;
        this.nextNode = nextNode;
    }
}

public class Main {
    static int V, E, K;
    static int[] minDistance;
    static List<List<Edge>> graph;
    static int INF = Integer.MAX_VALUE / 2;

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        minDistance = new int[V + 1];
        Arrays.fill(minDistance, INF);
        minDistance[K] = 0;
        graph = new ArrayList<>();
        for (int i = 0; i < V + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(s).add(new Edge(e, v));
        }
        dijkstra(K);
        for (int i = 1; i < V+1; i++) {
            int dist = minDistance[i];
            if (dist == INF) {
                System.out.println("INF");
            } else {
                System.out.println(dist);
            }
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.dist));
        minDistance[start] = 0;
        pq.add(new Node(start, 0));
        while (!pq.isEmpty()) {
            Node currNode = pq.poll();
            int currIndex = currNode.index;
            int currDist = currNode.dist;
            for (Edge nextEdge : graph.get(currIndex)) {
                int nextNode = nextEdge.nextNode;
                int nextDist = nextEdge.dist;
                if (currDist + nextDist < minDistance[nextNode]) {
                    pq.add(new Node(nextNode, currDist + nextDist));
                    minDistance[nextNode] = currDist + nextDist;
                }
            }
        }
    }
}
