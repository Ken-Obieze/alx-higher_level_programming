#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';
    for (let ht = 0; ht < this.height; ht++) {
      for (let wt = 0; wt < this.width; wt++) {
        output += 'X';
      }
      console.log(output);
      output = '';
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
