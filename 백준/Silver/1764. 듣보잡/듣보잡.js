const fs = require('fs');

// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const set = new Set();
const newSet = new Set();
for (let i = 0; i < N; i++) {
  const name = input[i + 1];
  set.add(name);
}
for (let i = 0; i < M; i++) {
  const newName = input[i + N + 1];
  if (set.has(newName)) {
    newSet.add(newName);
  }
}
console.log(newSet.size);
const names = [...newSet].sort().forEach((e) => {
  console.log(e);
});
