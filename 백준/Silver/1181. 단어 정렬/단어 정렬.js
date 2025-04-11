const fs = require('fs');

//const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0], 10);
const words = Array.from(new Set(input.slice(1))).sort((a, b) => {
  return a.length == b.length ? a.localeCompare(b) : a.length - b.length;
});

// console.log(words);n
words.forEach((e) => console.log(e));
