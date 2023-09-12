#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv[2]));
}
