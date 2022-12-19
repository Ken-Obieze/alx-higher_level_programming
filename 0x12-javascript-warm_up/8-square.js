#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < x; i++) {
    let output = '';
    for (let j = 0; j < x; j++) {
      output += 'X';
    }
    console.log(output);
  }
} else {
  console.log('Missing size');
}
