#!/usr/bin/node

const argv = process.argv;

function factorial (n) {
  n = parseInt(n);
  if (isNaN(argv[2])) {
    return (1);
  }

  if (n === 1) {
    return (1);
  }

  return n * factorial(n - 1);
}

console.log(factorial(argv[2]));
