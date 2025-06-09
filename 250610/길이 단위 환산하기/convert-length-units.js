const fs = require("fs");
let ft = 30.48;
let n = Number(fs.readFileSync(0).toString());
result = n * ft;
console.log(result.toFixed(1));