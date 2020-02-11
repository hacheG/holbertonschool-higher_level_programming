#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
