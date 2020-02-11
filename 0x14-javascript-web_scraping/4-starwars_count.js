#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let count = 0;
  for (const q of body.results) {
    for (const w of q.characters) {
      if (w === 'https://swapi.co/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
