#!/usr/bin/node

const SquareTwo = require('./5-square');
module.exports = class Square extends SquareTwo {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
};
