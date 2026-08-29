const { add } = require('./src/app.js');
if(add(2,3) !== 5){ console.error('FAIL: 2+3 should be 5, got '+add(2,3)); process.exit(1); }
console.log('PASS 2+3=5');