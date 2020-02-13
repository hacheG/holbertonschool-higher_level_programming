#!/usr/bin/node

const fs = require('fs');

fs.readFile('/Users/joe/test.txt', (err, data) => {
		  if (err) {
		      console.error(err)
		          return
			    }
			      console.log(data)
			      });
