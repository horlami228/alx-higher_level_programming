#!/usr/bin/node

const argv = process.argv;

function secondBiggest (argv) {
  let max = parseInt(argv[2]);
  let secondMax = parseInt(argv[3]);

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
    const num = parseInt(argv[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}

secondBiggest(argv);
