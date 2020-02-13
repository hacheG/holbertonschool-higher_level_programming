#!/usr/bin/node

const fs = require('fs');

<<<<<<< HEAD
fs.readFile('/Users/joe/test.txt', (err, data) => {
		  if (err) {
		      console.error(err)
		          return
			    }
			      console.log(data)
			      });
=======
fs.readFile(process.argv[2], { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
>>>>>>> 14b92c1081f6c1b2afe893bec73776102cc1f88e
