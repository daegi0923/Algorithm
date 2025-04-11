const fs = require('fs');

// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, S] = input[0].split(' ').map(Number);
const seq = input[1].split(' ').map(Number);

let sum = 0;
let left = 0;
let minLength = Infinity;

for (let right = 0; right < N; right++) {
  sum += seq[right];

  while (sum >= S) {
    minLength = Math.min(minLength, right - left + 1);
    sum -= seq[left];
    left++;
  }
}

console.log(minLength === Infinity ? 0 : minLength);
