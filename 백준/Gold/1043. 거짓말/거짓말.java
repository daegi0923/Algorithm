import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static List<List<Integer>> parties;
    static int[] parents;
    static Set<Integer> truthRoot = new HashSet<>();


    public static int find(int x) {
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    public static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA != rootB) {
            parents[rootB] = rootA;
        }
    }

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        parties = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        int truthCount = Integer.parseInt(st.nextToken());
        parents = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            parents[i] = i;
        }
        List<Integer> truthPeople = new ArrayList<>();

        for (int i = 0; i < truthCount; i++) {
            int person = Integer.parseInt(st.nextToken());
            truthPeople.add(person);
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int partySize = Integer.parseInt(st.nextToken());
            List<Integer> party = new ArrayList<>();
            for (int j = 0; j < partySize; j++) {
                party.add(Integer.parseInt(st.nextToken()));
            }
            parties.add(party);
            for (int j = 1; j < partySize; j++) {
                union(party.get(0), party.get(j));
            }
        }
//        Arrays.stream(parents).forEach(e -> {
//            System.out.print(e + " ");
//        });

        for(int person : truthPeople){
            truthRoot.add(find(person));
        }
        int ans = 0;
//        System.out.println(truthRoot);
        for (List<Integer> party : parties) {
            boolean canLie = true;
//            System.out.println(party);
            for (int person : party) {
                if (truthRoot.contains(find(person))) {
                    canLie = false;
                    break;
                }
            }
            if (canLie) {
                ans = ans + 1;
            }
        }
        System.out.println(ans);
    }
}
