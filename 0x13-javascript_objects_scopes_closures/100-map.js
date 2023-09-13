#!/usr/bin/node
const { list } = require('./100-data');
const mapped = list.map((x) => { return x * list.indexOf(x); });
console.log(mapped);
console.log(list);
