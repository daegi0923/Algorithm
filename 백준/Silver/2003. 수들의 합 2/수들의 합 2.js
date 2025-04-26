const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map((e) => Number(e));
const seq = input[1].split(' ').map((e) => Number(e));

let left = 0;
let right = 0;
let localSum = seq[0];
let ans = 0;
while (left < N) {
  if (localSum === M) ans = ans + 1;
  
  if(localSum >= M){
    localSum = localSum - seq[left]
    left = left + 1
  }
  else{
    right= right + 1
    if(right === N) break;
    localSum = localSum + seq[right]
  }
}
console.log(ans);
