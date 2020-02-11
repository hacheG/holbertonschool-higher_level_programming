#!/usr/bin/node
const request = require('request'); 

const num = process.argv[2];
const url = 'https://swapi.co/api/films/' + num;

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }  
  console.log(body.title);
});
