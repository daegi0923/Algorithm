import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        String S = br.readLine();
        String target = "IO".repeat(N) + "I";
//        System.out.println(target);
//        System.out.println(S);
        int count = 0;
        for(int i = 0;i<M-(2*N+1)+1;i++){
            String subString = S.substring(i, i+(2*N+1));
//            System.out.println(subString +" "+target );

            if(subString.equals(target)){
                count = count + 1;
            }
        }
        System.out.println(count);
    }
}
