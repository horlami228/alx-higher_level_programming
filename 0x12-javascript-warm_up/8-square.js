#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);

if (argv[2] === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < num; count++) {
    console.log('X'.repeat(num));
  }
}
