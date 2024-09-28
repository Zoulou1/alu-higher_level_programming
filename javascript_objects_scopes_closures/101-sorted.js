#!/usr/bin/node
const data = require('./101-data').dict;

const newDict = {};

for (const [userId, occurrences] of Object.entries(data)) {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

console.log(newDict);
