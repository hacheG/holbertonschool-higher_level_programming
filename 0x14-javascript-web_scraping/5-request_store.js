#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request('http://loripsum.net/api', (err, res, body) => {
  if (err) { return console.log(err); }

  fs.appendFile('loripsum', body, (err) => {
    if (err) throw err;
    console.log('The "data to append" was appended to file!');
  });
});
