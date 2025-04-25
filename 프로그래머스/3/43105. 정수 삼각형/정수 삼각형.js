function solution(triangle) {
  const N = triangle.length;
  const dp = Array.from({ length: N }, () => Array(N).fill(0));

  for (let i = N - 1; i >= 0; i--) {
    for (let j = 0; j <= i; j++) {
      if (i === N - 1) {
        dp[i][j] = triangle[i][j]; // 마지막 줄 초기화
      } else {
        dp[i][j] = triangle[i][j] + Math.max(dp[i + 1][j], dp[i + 1][j + 1]);
      }
    }
  }

  return dp[0][0];
}
