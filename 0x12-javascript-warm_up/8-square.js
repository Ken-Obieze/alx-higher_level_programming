#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      console.log('X');
    }
  }
} else {
  console.log('Missing size');
}
