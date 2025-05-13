const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const arr = input[1].split(' ').map((e) => Number(e));

arr.sort((a, b) => {
  return a - b;
});
let ans = 0;
arr.forEach((e, i) => {
  const target = e;
  let left = 0;
  let right = N - 1;
  while (left < right) {
    if (right === i) {
      right = right - 1;
      continue;
    }
    if (left === i) {
      left = left + 1;
      continue;
    }

    if (arr[left] + arr[right] < target) {
      left = left + 1;
    } else if (arr[left] + arr[right] === target) {
      ans = ans + 1;
      break;
    } else {
      right = right - 1;
    }
  }
});
console.log(ans);
