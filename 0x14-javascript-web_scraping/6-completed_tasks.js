#!/usr/bin/node
const request = require('request');
request(process.arg[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let count = 0;
  let counTen = 0;
  const a = {};
  for (let i = 0; i < body.length; i++) {
    counTen += 1;
    if (body[i].completed === true) {
      count += 1;
      a[body[i].userId] = count;
    }
    if (counTen === 20) {
      count = 0;
      counTen = 0;
    }
  }
  console.log(a);
});
