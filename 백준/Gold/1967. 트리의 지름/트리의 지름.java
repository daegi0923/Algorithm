import java.io.*;
import java.util.*;


class Node {
    int to;
    int weight;

    Node(int to, int weight) {
        this.to = to;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return this.to + " " + this.weight;
    }
}

public class Main {
    static int n;

    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    static boolean[] visited1;
    static boolean[] visited2;

    static int maxDist1, maxDist2, maxNode1, maxNode2 = 0;

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        visited1 = new boolean[n + 1];
        visited2 = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
//        System.out.println(n);
        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(parent).add(new Node(child, weight));
            graph.get(child).add(new Node(parent, weight));

        }
//        System.out.println(graph);
        visited1[1] = true;
        dfs(1, 0, 1);
//        System.out.println(maxNode1);
        visited2[maxNode1] = true;
        dfs(maxNode1, 0, maxNode1);
        System.out.println(maxDist2);
    }

    public static void dfs(int here, int sumWeight, int start) {
//        System.out.println(here);
        if (start == 1) {
            if (maxDist1 < sumWeight) {
                maxNode1 = here;
                maxDist1 = sumWeight;
            }
        } else {
            if (maxDist2 < sumWeight) {
                maxDist2 = sumWeight;
                maxNode2 = here;
            }
        }
        for (Node nextNode : graph.get(here)) {
            if (start == 1) {
                if (visited1[nextNode.to]) continue;
                visited1[nextNode.to] = true;
                dfs(nextNode.to, sumWeight + nextNode.weight, start);

            } else{
                if (visited2[nextNode.to]) continue;
                visited2[nextNode.to] = true;
                dfs(nextNode.to, sumWeight + nextNode.weight, start);

            }
        }

    }
}
