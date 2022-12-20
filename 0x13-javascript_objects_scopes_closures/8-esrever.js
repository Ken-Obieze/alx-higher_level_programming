#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  while (list.length > 0) {
    revList.push(list.pop());
  }
  return revList;
};
