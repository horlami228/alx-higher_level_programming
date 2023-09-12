#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  for (let count = 0; count < parseInt(argv[2]); count++) {
    console.log('C is fun');
  }
}
