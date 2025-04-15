const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
let seq = 0;
let result = ""
const personList = input
  .slice(1)
  .map((e) => {
    const [age, name] = e.split(' ');
    seq = seq + 1;
    return { age, name, seq };
  })
  .sort((a, b) => {
    return a.age === b.age ? a.seq - b.seq : a.age - b.age;
  })
  .forEach((e) => {
    result = result + `${e.age} ${e.name}\n`
  });
  console.log(result)
