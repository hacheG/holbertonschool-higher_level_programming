#!/usr/bin/node
const Rectangle = require('/.4-Rectangle');
module.exports =
class Square extends Rectangle{
  constructor (size) {
  super (size, size);
  }
};