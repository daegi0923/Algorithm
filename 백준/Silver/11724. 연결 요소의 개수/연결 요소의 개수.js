const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const graph = Array.from({length : N+1}, ()=>[])
// console.log(h)
for(let i=0; i< M; i++){
  const [u, v] = input[i+1].split(' ').map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

const visited = Array(N+1).fill(false)

function bfs(start){
  const queue = [start];
  visited[start] = true;
  while(queue.length > 0){
    const node = queue.shift();
    for(const neighbor of graph[node]){
      if(!visited[neighbor]){
        visited[neighbor] = true;
        queue.push(neighbor)
      }
    }
  }

}

let count = 0;
for(let i = 1; i <= N; i++){
  if(!visited[i]){
    bfs(i);
    count = count + 1;
  }
}

console.log(count)