import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String target = br.readLine();

        StringBuilder sb = new StringBuilder();

        int tLen = target.length();

        for (int i = 0; i < str.length(); i++) {
            sb.append(str.charAt(i));

            // target의 끝 글자와 현재 문자가 같을 때만 검사
            if (sb.length() >= tLen) {
                boolean isSame = true;
                for (int j = 0; j < tLen; j++) {
                    if (sb.charAt(sb.length() - tLen + j) != target.charAt(j)) {
                        isSame = false;
                        break;
                    }
                }
                if (isSame) {
                    sb.delete(sb.length() - tLen, sb.length()); // 폭발!
                }
            }
        }

        System.out.println(sb.length() == 0 ? "FRULA" : sb.toString());
    }
}
