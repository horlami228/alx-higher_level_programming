#!/usr/bin/node

const fs = require('fs');

const FileName = process.argv[2];
const string = process.argv[3];

fs.writeFile(FileName, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
}
);
