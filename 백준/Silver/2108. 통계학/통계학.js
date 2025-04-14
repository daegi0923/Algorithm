const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0], 10);
const numbers = input.slice(1).map(Number).sort((a, b) => a - b);

let output = "";

// 산술평균 (반올림 + -0 방지)
const sum = numbers.reduce((acc, val) => acc + val, 0);
let avg = Math.round(sum / N);
if (Object.is(avg, -0)) avg = 0;
output += `${avg}\n`;

// 중앙값
output += `${numbers[Math.floor(N / 2)]}\n`;

// 최빈값
const freq = new Map();
let maxFreq = 0;
for (let num of numbers) {
  const count = (freq.get(num) || 0) + 1;
  freq.set(num, count);
  maxFreq = Math.max(maxFreq, count);
}
const modes = [...freq.entries()]
  .filter(([_, count]) => count === maxFreq)
  .map(([num]) => num)
  .sort((a, b) => a - b);
output += `${modes.length > 1 ? modes[1] : modes[0]}\n`;

// 범위
output += `${numbers[numbers.length - 1] - numbers[0]}\n`;

// 한 번에 출력
console.log(output);
