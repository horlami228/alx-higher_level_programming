#!/usr/bin/node

const { list } = require('./100-data');
console.log(list);
const mapped = list.map((x) => { return x * list.indexOf(x); });
console.log(mapped);
