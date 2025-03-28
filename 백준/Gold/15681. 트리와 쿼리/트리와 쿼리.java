import com.sun.source.tree.Tree;

import java.io.*;
import java.sql.Array;
import java.util.*;

class Node {
    int index;
    int depth;
    List<Integer> children = new ArrayList<>();

    Node(int index) {
        this.index = index;
    }

    public void addChild(int child) {
        this.children.add(child);
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }

    @Override
    public String toString() {
        return "Node{" +
                "index=" + index +
                ", depth=" + depth +
                ", children=" + children +
                '}';
    }
}

public class Main {
    static int N, R, Q;
    static int[] dp;
    static List<Node> tree = new ArrayList<>();
    static List<List<Integer>> graph = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N + 1; i++) {
            tree.add(new Node(i));
            graph.add(new ArrayList<>());
        }
        dp = new int[N+1];
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            graph.get(U).add(V);
            graph.get(V).add(U);
        }
        bfs(R);
//        System.out.println(tree);
        tree.sort((a, b) -> b.depth - a.depth);
        for(Node n:tree){
//            System.out.println(n);
            if(n.children.isEmpty()){
                dp[n.index] = 1;
            }
            else{
                int sum = 0;
                for(int c:n.children){
                    sum = sum + dp[c];
                }
//                System.out.println(sum);
                dp[n.index] = sum + 1;
            }
        }
        for(int q = 0;q<Q;q++){
            int U = Integer.parseInt(br.readLine());
            System.out.println(dp[U]);
        }
    }

    static void bfs(int start) {
        boolean[] visited = new boolean[N + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(R);
        visited[start] = true;
        tree.get(start).setDepth(0);
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            int depth = tree.get(curr).depth;
            for (int nextIdx : graph.get(curr)) {
                if (!visited[nextIdx]) {
                    visited[nextIdx] = true;
                    tree.get(curr).addChild(nextIdx);
                    tree.get(nextIdx).setDepth(depth + 1);
                    queue.add(nextIdx);
                }
            }
        }
    }
}
