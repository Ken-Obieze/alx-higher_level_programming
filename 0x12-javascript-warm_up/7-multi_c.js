#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < num; i++) {
    console.log('Cis fun');
  }
} else {
  console.log('Missing number of occurences');
}
