#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  a = parseInt(argv[2]);
  b = parseInt(argv[3]);

  console.log(a + b);
}

add();
