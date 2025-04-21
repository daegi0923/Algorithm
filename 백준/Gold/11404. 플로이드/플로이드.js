const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const M = parseInt(input[1]);
const dist = Array.from({ length: N + 1 }, () => Array(N + 1).fill(Infinity));
for (let i = 0; i < M; i++) {
  const [from, to, cost] = input[i + 2].split(' ').map((e) => Number(e));
  // console.log(from, to, cost, graph[from][to])
  if (dist[from][to] > cost) {
    dist[from][to] = cost;
  }
}
for (let k = 1; k < N + 1; k++) {
  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      if (dist[i][k] + dist[k][j] < dist[i][j]) {
        dist[i][j] = dist[i][k] + dist[k][j];
      }
    }
  }
}
const result = dist.slice(1).map(e=>e.slice(1))
result.forEach((line, i)=>{
  line.forEach((_, j)=>{
    if(i == j||result[i][j] === Infinity) result[i][j] = 0
    
  })
})
result.forEach(line=>{
  console.log(line.join(' '))
})
