#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < x; i++) {
    console.log('Cis fun');
  }
} else {
  console.log('Missing number of occurrences');
}
