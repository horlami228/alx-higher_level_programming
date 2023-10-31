#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const FilePath = process.argv[3];
let content = '';

request(url, (err, response, body) => {
  if (err) {
    console.error('error:', err);
  } else {
    content = body;

    fs.writeFile(FilePath, content, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
