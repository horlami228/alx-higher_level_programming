#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
let count = 0;

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    const DataLen = data.results.length;
    // loop through the results
    for (let i = 0; i < DataLen; i++) {
      const char = data.results[i].characters;

      for (let j = 0; j < char.length; j++) {
        const check = char[j].endsWith('18/');
        if (check) {
          count++;
        }
      }
    }

    console.log(count);
  }
});
