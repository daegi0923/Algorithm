const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// console.log(input);
const N = Number(input[0]);
const graph = Array.from({ length: N }, () => {
  return Array(N).fill(0);
});
const arr = Array(10);
const visited = Array.from({ length: N }, () => {
  return Array(N).fill(0);
});
for (let i = 0; i < N; i++) {
  const line = input[i + 1].split(' ');
  line.forEach((e, j) => {
    graph[i][j] = Number(e);
  });
}
for (let k = 0; k < N; k++) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (graph[i][k] && graph[k][j]) {
        graph[i][j] = 1;
      }
    }
  }
}
const result = graph.map((row) => row.join(' ')).join('\n');
console.log(result);
