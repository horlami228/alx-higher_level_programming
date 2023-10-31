#!/usr/bin/node

const request = require('request');
const MovieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + MovieId, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
