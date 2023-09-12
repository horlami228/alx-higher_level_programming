#!/usr/bin/node

const argv = process.argv;

function secondBiggest (argv) {
  let max = argv[2];
  let secondMax = argv[3];

  if (argv.length === 2 || argv.length === 3) {
    console.log(0);
    return;
  }

  if (secondMax > max) {
    const temp = max;
    max = secondMax;
    secondMax = temp;
  }

  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > max) {
      secondMax = max;
      max = argv[i];
    } else if (argv[i] > secondMax && argv[i] !== max) {
      secondMax = argv[i];
    }
  }

  console.log(secondMax);
}

secondBiggest(argv);
