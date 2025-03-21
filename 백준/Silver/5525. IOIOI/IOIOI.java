import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine()); // PN의 N값
        int M = Integer.parseInt(br.readLine()); // 문자열 길이
        String S = br.readLine(); // 문자열

        int count = 0; // PN의 개수
        int i = 0;
        int pattern = 0; // 현재 연속된 "IOI" 패턴의 개수

        while (i < M - 1) {
            // "IOI" 패턴 시작 확인
            if (S.charAt(i) == 'I' && S.charAt(i + 1) == 'O' && i + 2 < M && S.charAt(i + 2) == 'I') {
                pattern++;
                if (pattern == N) {
                    count++;
                    pattern--; // 다음 가능한 PN 찾기 위해 1개 빼고 계속
                }
                i += 2; // "OI"가 끝났으므로 다음 "O"를 위해 2칸 이동
            } else {
                pattern = 0; // 패턴 끊기면 초기화
                i++; // 다음으로 한 칸 이동
            }
        }

        System.out.println(count);
    }
}
