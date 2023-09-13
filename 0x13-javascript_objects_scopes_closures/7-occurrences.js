#!/usr/bin/node

exports.nbOccurences = function (list, searcElement) {
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searcElement) {
      count++;
    }
  }

  return count;
};
